#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.total = 0 
        self.discount = 0  
        self.last_transaction = 0  

    def add_item(self, item_price):
        self.total += item_price
        self.last_transaction = item_price

    def apply_discount(self, discount_percentage):
        discount_factor = float(discount_percentage) / 100

        self.total -= self.total * discount_factor

    def void_last_transaction(self):
        self.total -= self.last_transaction


register = CashRegister()

register.add_item(10)
register.add_item(15)

print("total", register.total)