"""Порядок работы с заказом. Правила в domain, SQL в storage."""
from . import domain
from .errors import success, failure

PURCHASE_MESSAGES = {
    "OUT_OF_STOCK": "Выбранного размера нет или товара недостаточно",
    "USER_LIMIT_EXCEEDED": "Превышен лимит покупки",
    "INSUFFICIENT_COINS": "Недостаточно коинов",
}

def create_order(storage, user_id, product_id, size, quantity):
    with storage.transaction():
        user = storage.get_user(user_id)
        if user is None:
            return failure("USER_NOT_FOUND", "Участник не найден")
        product = storage.get_product(product_id)
        if product is None:
            return failure("PRODUCT_NOT_FOUND", "Товар не найден")

        total = domain.calculate_total(product["price_coins"], quantity)
        owned = storage.count_owned(user_id, product_id)
        code = domain.purchase_error(product, size, quantity, user["coins"], owned, total)
        if code is not None:
            return failure(code, PURCHASE_MESSAGES[code])

        order = storage.create_order(user_id, product_id, size, quantity, total)
        return success({
            "order_id": order["id"],
            "status": order["status"],
            "total_price": order["total_price"],
        })

def cancel_order(storage, order_id):
    with storage.transaction():
        order = storage.get_order(order_id)
        if order is None:
            return failure("ORDER_NOT_FOUND", "Заказ не найден")
        if not domain.can_cancel(order):
            return failure("ORDER_STATUS_ERROR", "Этот заказ нельзя отменить")
        cancelled = storage.cancel_order(order, domain.refund_amount(order["total_price"]))
        return success({"order_id": cancelled["id"], "status": cancelled["status"]})

def confirm_pickup(storage, order_id):
    with storage.transaction():
        order = storage.get_order(order_id)
        if order is None:
            return failure("ORDER_NOT_FOUND", "Заказ не найден")
        if not domain.can_pickup(order):
            return failure("ORDER_STATUS_ERROR", "Этот заказ нельзя выдать")
        picked_up = storage.confirm_pickup(order_id)
        return success({"order_id": picked_up["id"], "status": picked_up["status"]})

