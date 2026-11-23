"""SQLite. Write methods are called after the rules have been checked."""
import sqlite3
import uuid
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
        'A list of products in id order.'
        # TODO: finish this function.
        raise NotImplementedError("list_products")

    def get_user(self, user_id):
        'A dict with id, coins or None. Reading does not create a user.'
        # TODO: finish this function.
        raise NotImplementedError("get_user")

    def get_order(self, order_id):
        'A dict with all the orders fields or None.'
        # TODO: finish this function.
        raise NotImplementedError("get_order")

    def count_owned(self, user_id, product_id):
        'The number of units of the product in created and picked_up, across all sizes.'
        # TODO: finish this function.
        raise NotImplementedError("count_owned")

    def create_order(self, user_id, product_id, size, quantity, total_price):
        'Write the order, the balance, and the stock in one transaction. Return the order.'
        # TODO: finish this function.
        raise NotImplementedError("create_order")

    def cancel_order(self, order, refund):
        'Return the given amount and the product, change the status in one transaction.'
        # TODO: finish this function.
        raise NotImplementedError("cancel_order")

    def confirm_pickup(self, order_id):
        'Change only the status. The balance and the stock were already reduced at purchase.'
        # TODO: finish this function.
        raise NotImplementedError("confirm_pickup")

