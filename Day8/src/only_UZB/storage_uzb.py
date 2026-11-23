"""SQLite. Yozish metodlari qoidalar tekshirilgandan keyin chaqiriladi."""
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
        'id tartibidagi tovarlar ro‘yxati.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("list_products")

    def get_user(self, user_id):
        'id, coins lug‘ati yoki None. O‘qish foydalanuvchi yaratmaydi.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("get_user")

    def get_order(self, order_id):
        'orders ning barcha maydonlari bor lug‘at yoki None.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("get_order")

    def count_owned(self, user_id, product_id):
        'Barcha o‘lchamlar bo‘yicha created va picked_up dagi tovar birliklari soni.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("count_owned")

    def create_order(self, user_id, product_id, size, quantity, total_price):
        'Buyurtma, balans va qoldiqni bitta tranzaksiyada yozish. Buyurtmani qaytarish.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("create_order")

    def cancel_order(self, order, refund):
        'Berilgan summa va tovarni qaytarish, holatni bitta tranzaksiyada o‘zgartirish.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("cancel_order")

    def confirm_pickup(self, order_id):
        'Faqat holatni o‘zgartirish. Balans va qoldiq xaridda allaqachon kamaytirilgan.'
        # TODO: bu funksiyani tugating.
        raise NotImplementedError("confirm_pickup")

