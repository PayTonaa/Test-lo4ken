class ProductInventory:
    product_name = ""
    product_category = ""
    quantity_available = 0
    unit_price = 0.0
    def addProduct(self, product_name, product_category, quantity_available, unit_price):
        self.product_name = product_name
        self.product_category = product_category
        self.quantity_available = quantity_available
        self.unit_price = unit_price

    def showInventory(self):
        if self.quantity_available > 0:
            print(f"{self.product_name}, {self.product_category}, {self.quantity_available}, {self.unit_price}")

    def sellProduct(self, number):
        if self.quantity_available - number >= 0:
            self.quantity_available -= number
        else:
            print("not enought")

products_data = [
    ["Laptop", "Elektronika", 10, 2500.00],
    ["Koszula", "Odzież", 50, 80.00],
    ["Sok pomarańczowy", "Spożywcze", 20, 5.00],
    ["Buty sportowe", "Obuwie", 30, 200.00]
]
products = []

for prodct in products_data:
    zadanie = ProductInventory()
    zadanie.addProduct(*prodct)
    products.append(zadanie)

for prodct in products:
    prodct.showInventory()
value = int(input("poda ilosc"))
id = input("podaj nazwe")
for prodct in products:
    if prodct.product_name == id:
        prodct.sellProduct(value)
        prodct.showInventory()
