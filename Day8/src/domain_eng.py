"""Rules without SQL and MCP. All arithmetic is in whole coins."""

def calculate_total(price, quantity):
    'The order cost.'
    # TODO: finish this function.
    raise NotImplementedError("calculate_total")

def purchase_error(product, size, quantity, balance, already_owned, total):
    'A refusal code or None. The user and the product have already been found.'
    # TODO: finish this function.
    raise NotImplementedError("purchase_error")

def refund_amount(total_price):
    'The refund amount based on the saved order cost.'
    # TODO: finish this function.
    raise NotImplementedError("refund_amount")

def can_cancel(order):
    'Whether the found order can be cancelled.'
    # TODO: finish this function.
    raise NotImplementedError("can_cancel")

def can_pickup(order):
    'Whether the found order can be picked up.'
    # TODO: finish this function.
    raise NotImplementedError("can_pickup")

