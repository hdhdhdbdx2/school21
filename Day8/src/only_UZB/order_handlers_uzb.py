"""Buyurtma bilan ishlash tartibi. Qoidalar domain ichida, SQL storage ichida."""
from . import domain
from .errors import success, failure

def create_order(storage, user_id, product_id, size, quantity):
    'Do‘kon qoidalari va kelishilgan metodlar bo‘yicha amalga oshiring.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("create_order")

def cancel_order(storage, order_id):
    'Do‘kon qoidalari va kelishilgan metodlar bo‘yicha amalga oshiring.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("cancel_order")

def confirm_pickup(storage, order_id):
    'Do‘kon qoidalari va kelishilgan metodlar bo‘yicha amalga oshiring.'
    # TODO: bu funksiyani tugating.
    raise NotImplementedError("confirm_pickup")

