
class ProductInventory:
    def __init__(self):
        self.product_name = ""
        self.product_category = ""
        self.quantity_available = 0
        self.unit_price = 0.0

    def addProduct(self, name, category, quantity, price):
        self.product_name = name
        self.product_category = category
        self.quantity_available = quantity
        self.unit_price = price

    def showInventory(self):
        if self.quantity_available > 0:
            print(f"Product: {self.product_name}, Category: {self.product_category}, "
                  f"dostepne: {self.quantity_available}, Unit Price: {self.unit_price:.2f}")

    def sellProduct(self, sold_quantity):
        if self.quantity_available >= sold_quantity:
            self.quantity_available -= sold_quantity
        else:
            print("za mało produktu")

tab = []
products_data = [
    ["Laptop", "Elektronika", 10, 2500.00],
    ["Koszula", "Odzież", 50, 80.00],
    ["Sok pomarańczowy", "Spożywcze", 20, 5.00],
    ["Buty sportowe", "Obuwie", 30, 200.00]
]

for produkt in products_data:
    zadanie = ProductInventory()
    zadanie.addProduct(produkt[0], produkt[1], produkt[2], produkt[3])
    tab.append(zadanie)

for produkt in tab:
    produkt.showInventory()

product_to_sell = input("Podaj nazwę produktu do sprzedaży: ")
for produkt in tab:
    if produkt.product_name == product_to_sell:
        quantity_to_sell = int(input(f"Ile sztuk {product_to_sell} chcesz sprzedać? "))
        produkt.sellProduct(quantity_to_sell)
