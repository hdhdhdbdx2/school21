import sqlite3
from pathlib import Path

import pytest

from src.domain import calculate_total
from src.order_handlers import create_order
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
