"""O‘qish vositalari. Bu yerda SQL yo‘q."""
from .errors import success, failure

def get_product(storage, product_id):
    product = storage.get_product(product_id)
    if product is None:
        return failure("PRODUCT_NOT_FOUND", "Tovar topilmadi")
    return success(product)

def list_products(storage):
    'Do‘kon qoidalari va kelishilgan metodlar bo‘yicha amalga oshiring.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("list_products")

def get_coin_balance(storage, user_id):
    'Do‘kon qoidalari va kelishilgan metodlar bo‘yicha amalga oshiring.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("get_coin_balance")

def get_order_status(storage, order_id):
    'Do‘kon qoidalari va kelishilgan metodlar bo‘yicha amalga oshiring.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("get_order_status")

