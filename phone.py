from item import Item
class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)

        # def __repr__(self):
            # return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"

phone1 = Phone("jscPhoneV10", 500, 5, 1)
# phone1.broken_phones = 1
print(phone1.calculate_total_price())

phone2 = Phone("jscPhoneV20", 700, 5, 1)
# phone2.broken_phones = 1

print(Item.all)
print(Phone.all)
