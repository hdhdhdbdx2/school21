"""SQL va MCPsiz qoidalar. Barcha hisob-kitob butun koinlarda."""

def calculate_total(price, quantity):
    'Buyurtma qiymati.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("calculate_total")

def purchase_error(product, size, quantity, balance, already_owned, total):
    'Rad etish kodi yoki None. Foydalanuvchi va tovar allaqachon topilgan.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("purchase_error")

def refund_amount(total_price):
    'Buyurtmaning saqlangan qiymati bo‘yicha qaytarish summasi.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("refund_amount")

def can_cancel(order):
    'Topilgan buyurtmani bekor qilish mumkinmi.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("can_cancel")

def can_pickup(order):
    'Topilgan buyurtmani berish mumkinmi.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("can_pickup")

