"""SQLite. Методы записи вызываются после проверки правил."""
import sqlite3
import uuid
from contextlib import contextmanager
from pathlib import Path

class Storage:
    def __init__(self, db_path, seed_path):
        self.path = Path(db_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        is_new = not self.path.exists()
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        if is_new:
            self.connection.executescript(Path(seed_path).read_text(encoding="utf-8"))
            self.connection.commit()

    def close(self):
        self.connection.close()

    @contextmanager
    def transaction(self):
        """Hold the write lock from validation through the final update."""
        if self.connection.in_transaction:
            yield
            return
        with self.connection:
            self.connection.execute("BEGIN IMMEDIATE")
            yield

    def get_product(self, product_id):
        row = self.connection.execute(
            "SELECT id, name, price_coins, user_limit FROM products WHERE id = ?",
            (product_id,),
        ).fetchone()
        if row is None:
            return None
        product = dict(row)
        rows = self.connection.execute(
            "SELECT size, quantity FROM stock WHERE product_id = ? ORDER BY size",
            (product_id,),
        ).fetchall()
        product["stock"] = {r["size"]: r["quantity"] for r in rows}
        return product

    def list_products(self):
        'Список товаров в порядке id.'
        rows = self.connection.execute("SELECT id FROM products ORDER BY id").fetchall()
        return [self.get_product(row["id"]) for row in rows]

    def get_user(self, user_id):
        'Словарь id, coins или None. Чтение не создаёт пользователя.'
        row = self.connection.execute(
            "SELECT id, coins FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row is not None else None

    def get_order(self, order_id):
        'Словарь со всеми полями orders или None.'
        row = self.connection.execute(
            """SELECT id, user_id, product_id, size, quantity, total_price, status
               FROM orders WHERE id = ?""",
            (order_id,),
        ).fetchone()
        return dict(row) if row is not None else None

    def count_owned(self, user_id, product_id):
        'Число единиц товара в created и picked_up, по всем размерам.'
        row = self.connection.execute(
            """SELECT COALESCE(SUM(quantity), 0)
               FROM orders
               WHERE user_id = ? AND product_id = ? AND status IN ('created', 'picked_up')""",
            (user_id, product_id),
        ).fetchone()
        return row[0]

    def create_order(self, user_id, product_id, size, quantity, total_price):
        'Записать заказ, баланс и остаток одной транзакцией. Вернуть заказ.'
        order_id = uuid.uuid4().hex
        with self.transaction():
            self.connection.execute(
                """INSERT INTO orders (id, user_id, product_id, size, quantity, total_price, status)
                   VALUES (?, ?, ?, ?, ?, ?, 'created')""",
                (order_id, user_id, product_id, size, quantity, total_price),
            )
            self.connection.execute(
                "UPDATE users SET coins = coins - ? WHERE id = ?",
                (total_price, user_id),
            )
            self.connection.execute(
                "UPDATE stock SET quantity = quantity - ? WHERE product_id = ? AND size = ?",
                (quantity, product_id, size),
            )
            return self.get_order(order_id)

    def cancel_order(self, order, refund):
        'Вернуть переданную сумму и товар, поменять статус одной транзакцией.'
        # TODO: закончите эту функцию.
        raise NotImplementedError("cancel_order")

    def confirm_pickup(self, order_id):
        'Изменить только статус. Баланс и остаток уже уменьшены при покупке.'
        # TODO: закончите эту функцию.
        raise NotImplementedError("confirm_pickup")

