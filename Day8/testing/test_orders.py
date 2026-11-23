import sqlite3
from pathlib import Path

import pytest

from src.domain import calculate_total
from src.order_handlers import cancel_order, confirm_pickup, create_order
from src.storage import Storage


@pytest.fixture
def storage(tmp_path):
    seed = Path(__file__).resolve().parents[1] / "data" / "seed.sql"
    database = Storage(tmp_path / "test.db", seed)
    try:
        yield database
    finally:
        database.close()


def snapshot(storage):
    connection = storage.connection
    return (
        connection.execute("SELECT * FROM products ORDER BY id").fetchall(),
        connection.execute("SELECT * FROM stock ORDER BY product_id, size").fetchall(),
        connection.execute("SELECT * FROM users ORDER BY id").fetchall(),
        connection.execute("SELECT * FROM orders ORDER BY id").fetchall(),
    )


def test_price_times_quantity():
    assert calculate_total(150, 2) == 300


def test_insufficient_coins_changes_no_table(storage):
    before = snapshot(storage)
    result = create_order(storage, "student_poor", "hoodie", "M", 1)

    assert result["ok"] is False
    assert result["error"]["code"] == "INSUFFICIENT_COINS"
    assert snapshot(storage) == before


def test_purchase_rolls_back_after_database_error(storage):
    before = snapshot(storage)
    with pytest.raises(sqlite3.IntegrityError):
        storage.create_order("student_01", "bottle", "one_size", 13, 150)

    assert snapshot(storage) == before


def test_cancel_refunds_original_price_once(storage):
    order_id = create_order(storage, "student_01", "bottle", "one_size", 1)["data"]["order_id"]
    with storage.connection:
        storage.connection.execute("UPDATE products SET price_coins = 180 WHERE id = 'bottle'")

    cancelled = cancel_order(storage, order_id)
    assert cancelled["data"] == {"order_id": order_id, "status": "cancelled"}
    assert storage.get_user("student_01")["coins"] == 1000
    assert storage.get_product("bottle")["stock"]["one_size"] == 12
    assert storage.count_owned("student_01", "bottle") == 0

    after_cancel = snapshot(storage)
    assert cancel_order(storage, order_id)["error"]["code"] == "ORDER_STATUS_ERROR"
    assert confirm_pickup(storage, order_id)["error"]["code"] == "ORDER_STATUS_ERROR"
    assert snapshot(storage) == after_cancel


def test_pickup_updates_only_status(storage):
    order_id = create_order(storage, "student_01", "bottle", "one_size", 1)["data"]["order_id"]
    catalog, stock, users, _ = snapshot(storage)

    picked_up = confirm_pickup(storage, order_id)
    assert picked_up["data"] == {"order_id": order_id, "status": "picked_up"}
    assert snapshot(storage)[:3] == (catalog, stock, users)
    assert storage.get_order(order_id)["status"] == "picked_up"

    after_pickup = snapshot(storage)
    assert confirm_pickup(storage, order_id)["error"]["code"] == "ORDER_STATUS_ERROR"
    assert cancel_order(storage, order_id)["error"]["code"] == "ORDER_STATUS_ERROR"
    assert snapshot(storage) == after_pickup


def test_reserve_threshold(storage):
    with storage.connection:
        storage.connection.execute("UPDATE users SET coins = 180 WHERE id = 'student_01'")
    before = snapshot(storage)
    declined = create_order(storage, "student_01", "bottle", "one_size", 1)
    assert declined["error"]["code"] == "INSUFFICIENT_COINS"
    assert snapshot(storage) == before

    with storage.connection:
        storage.connection.execute("UPDATE users SET coins = 200 WHERE id = 'student_01'")
    ordered = create_order(storage, "student_01", "bottle", "one_size", 1)
    assert ordered["data"]["total_price"] == 150
    assert storage.get_user("student_01")["coins"] == 50
