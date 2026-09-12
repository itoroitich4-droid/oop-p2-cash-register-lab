#!/usr/bin/env python3

class CashRegister:
  pass
    """A simple cash register model for adding items, applying discounts, and voiding transactions."""

    def __init__(self, discount=0):
        self.discount = discount if self._is_valid_discount(discount) else 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def _is_valid_discount(self, discount):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            return False
        return True

    def add_item(self, item, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * self.discount / 100
        self.total = self.total - discount_amount
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])

        if self.total < 0:
            self.total = 0
