"""Read tools. There is no SQL here."""
from .errors_eng import success, failure

def get_product(storage, product_id):
    product = storage.get_product(product_id)
    if product is None:
        return failure("PRODUCT_NOT_FOUND", "Product not found")
    return success(product)

def list_products(storage):
    'Implement according to the Shop rules and the agreed methods.'
    # TODO: finish this function.
    raise NotImplementedError("list_products")

def get_coin_balance(storage, user_id):
    'Implement according to the Shop rules and the agreed methods.'
    # TODO: finish this function.
    raise NotImplementedError("get_coin_balance")

def get_order_status(storage, order_id):
    'Implement according to the Shop rules and the agreed methods.'
    # TODO: finish this function.
    raise NotImplementedError("get_order_status")

