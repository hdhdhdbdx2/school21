"""The order workflow. The rules are in domain, the SQL is in storage."""
from . import domain_eng as domain
from .errors_eng import success, failure

def create_order(storage, user_id, product_id, size, quantity):
    'Implement according to the Shop rules and the agreed methods.'
    # TODO: finish this function.
    raise NotImplementedError("create_order")

def cancel_order(storage, order_id):
    'Implement according to the Shop rules and the agreed methods.'
    # TODO: finish this function.
    raise NotImplementedError("cancel_order")

def confirm_pickup(storage, order_id):
    'Implement according to the Shop rules and the agreed methods.'
    # TODO: finish this function.
    raise NotImplementedError("confirm_pickup")

