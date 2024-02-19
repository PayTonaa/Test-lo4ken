# class TaskList:
#     tittle = ""
#     description = ""
#     date = ""
#     completed = False
#     def addTask(self, tittle, description, date, completed):
#         self.tittle = tittle
#         self.description = description
#         self.date = date
#         self.completed = completed
#
#     def showTask(self, decyzja):
#         if self.completed == decyzja:
#             print(f"{self.tittle}, {self.description}, {self.date}, {self.completed}")
#
#
#     def taskComplete(self):
#         self.completed = True
#         print(f"{self.tittle}, {self.description}, {self.date}, {self.completed}")
#
#
# tab = []
# tasks_data = [
#     ["Zakupy spożywcze", "Kupić chleb i mleko", "2024-02-15", False],
#     ["Przygotowanie prezentacji", "Przygotować prezentację na spotkanie", "2024-02-20", False],
#     ["Sprzątanie mieszkania", "Wysprzątać pokój i umyć podłogę", "2024-02-18", True],
#     ["Zakupy online", "Zamówić nowe buty i koszulkę", "2024-02-17", False],
#     ["Nauka do egzaminu", "Powtórzyć materiał z matematyki", "2024-02-16", False]
# ]
# for task in tasks_data:
#     zadanie = TaskList()
#     zadanie.addTask(*task)
#     tab.append(zadanie)
#
# for task in tab:
#     task.showTask(True)
#
# for task in tab:
#     if task.tittle == "Zakupy spożywcze":
#         task.taskComplete()
#
# print("")
# for task in tab:
#     task.showTask(True)
#
#

#########################################################################
#
# class ProductInventory:
#     product_name = ""
#     product_category = ""
#     quantity_availabla = 0
#     unit_price = 0.0
#
#     def addProduct(self, product_name, product_category, quantity_availabla, unit_price):
#         self.product_name = product_name
#         self.product_category = product_category
#         self.quantity_availabla = quantity_availabla
#         self.unit_price = unit_price
#
#     def showInventory(self):
#         if self.quantity_availabla > 0:
#             print(f"{self.quantity_availabla}, {self.product_category}, {self.product_name}, {self.unit_price}")
#
#     def sellProduct(self, amount):
#         if self.quantity_availabla - amount < 0:
#             print("nie można sprzedać")
#         else:
#             self.quantity_availabla - amount
#             print(f"sprzedano {amount}")
#
# tab = []
# products_data = [
#     ["Laptop", "Elektronika", 10, 2500.00],
#     ["Koszula", "Odzież", 50, 80.00],
#     ["Sok pomarańczowy", "Spożywcze", 20, 5.00],
#     ["Buty sportowe", "Obuwie", 30, 200.00]
# ]
#
# for product in products_data:
#     zadanie = ProductInventory()
#     zadanie.addProduct(*product)
#     tab.append(zadanie)
#
# for product in tab:
#     product.showInventory()
#
# name = input("podaj produkt")
# for product in tab:
#     if product.product_name == name:
#         amount = int(input("podaj ilosc"))
#         product.sellProduct(amount)
#         print("")
#
# for product in tab:
#     product.showInventory()


# Stwórz klasę na nazwie Zwierze dodaj atrybuty takie jak imie, gatunek i wiek, płeć Następnie utwórz kilka obiektów tej klasy w
# tablicy reprezentujących rózenie zwierzęta takie jak pies kot i ryba

# Utwórz metodę wyświetlającą wszystkie informacje o zwierzęciu
# Wyświetl wszystkie zwierzęta płci męskiej
# wyświetrl zwierzę na podtawie podnaego imienia

# class Zwierze:
#     def construct(self, imie, gatunek, wiek, plec):
#         self.imie= imie
#         self.gatunek =  gatunek
#         self.wiek = wiek
#         self.plec = plec
#
#     def wyswietl(self):
#         print(f"{self.imie}, {self.gatunek}, {self.wiek}, {self.plec}")
#
# tab = []
# zwierzeta = [
#     ["Azor", "Pies", 12, "m"],
#     ["Nigga", "Kot", 1, "k"],
#     ["Glonojad", "Ryba", 5, "m"]]
#
# for animals in zwierzeta:
#     zadanie = Zwierze()
#     zadanie.construct(*animals)
#     tab.append(zadanie)
#
# for animals in tab:
#     if animals.plec == "m":
#         animals.wyswietl()
#
# imie = input("podaj imie")
# for animals in tab:
#     if animals.imie == imie:
#         animals.wyswietl()


# class Zwierze:
#     def __init__(self, imie, gatunek, wiek, plec):
#         self.imie = imie
#         self.gatunek = gatunek
#         self.wiek = wiek
#         self.plec = plec
#     def wyswietl(self):
#         print(f"{self.imie}, {self.gatunek}, {self.wiek}, {self.plec}")
#
# tab = []
# zwierzeta = [
#     ["Azor", "Pies", 12, "m"],
#     ["Nigga", "Kot", 1, "k"],
#     ["Glonojad", "Ryba", 5, "m"]]
#
# for zwierzaki in zwierzeta:
#     zadanie = Zwierze(*zwierzaki)
#     tab.append(zadanie)
#
# for zwierzaki in tab:
#     if zwierzaki.plec == "m":
#         zwierzaki.wyswietl()
#
# name = input("podaj imie ")
# for zwierzaki in tab:
#     if zwierzaki.imie == name:
#         zwierzaki.wyswietl()

# Zaimplementuj w języku Python klasę ZarzadzanieStudentami, która będzie zarządzać danymi dotyczącymi studentów na uczelni.
# Klasa ta powinna przechowywać informacje o studentach jako atrybuty klasy.
#
# Każdy student będzie reprezentowany jako instancja klasy Student. Klasa Student powinna zawierać atrybuty imię, nazwisko, nr_indeksu oraz oceny (lista ocen).
#
# Zdefiniuj następujące metody w klasie ZarzadzanieStudentami:
#
# dodaj_studenta(imie, nazwisko, nr_indeksu) - dodaje nowego studenta do listy studentów.
# usun_studenta(nr_indeksu) - usuwa studenta o podanym numerze indeksu z listy studentów.
# dodaj_ocene(nr_indeksu, ocena) - dodaje ocenę dla studenta o podanym numerze indeksu do listy ocen.
# pobierz_srednia(nr_indeksu) - zwraca średnią ocen studenta o podanym numerze indeksu.
# pobierz_studenta(nr_indeksu) - zwraca informacje o studencie o podanym numerze indeksu (imię, nazwisko, oceny).
# Upewnij się, że klasa ZarzadzanieStudentami jest odpowiednio zaprojektowana pod kątem hermetyzacji danych i obsługi wyjątków.
# class ZarzadzanieStudentami:
#
#     cache = []
#     def dodaj_studenta(self, imie, nazwisko, nr_indeksu, oceny):
#         student = {
#             "imie" : imie,
#             "nazwisko" : nazwisko,
#             "nr_indeksu" : nr_indeksu,
#             "oceny" : oceny}
#
#         self.cache.append(student)
#
#
#     def usun_studenta(self, number):
#         for student in self.cache:
#             if student["nr_indeksu"] == number:
#                 self.cache.remove(student)
#                 print("usunieto studenta")
#
#     def dodaj_ocene(self, nr_indeksu, ocena):
#         for numer in self.cache:
#             if numer["nr_indeksu"] == nr_indeksu:
#                 numer["ocena"].append(ocena)
#                 print("dodano ocene")
#
#     def pobierz_srednia(self, nr_indeksu):
#         for student in self.cache:
#             if student["nr_indeksu"] == nr_indeksu:
#                 oceny = student["oceny"]
#                 print(sum(oceny) / len(oceny))
#     def pobierz_studenta(self, nr_indeksu):
#         for numer in self.cache:
#             if numer["nr_indeksu"] == nr_indeksu:
#                 print(numer)
#
#
# students_array = [
#     ["Jan", "Kowalski", 123456, [4.0, 3.5, 4.5]],
#     ["Anna", "Nowak", 654321, [5.0, 4.5, 5.0]],
#     ["Katarzyna", "Wiśniewska", 987654, [3.0, 3.5, 3.0]],
#     ["Piotr", "Dąbrowski", 135792, [4.5, 4.0, 3.5]]
# ]
# zadanie = ZarzadzanieStudentami()
# for students in students_array:
#     zadanie.dodaj_studenta(*students)
# number = 654321
# zadanie.usun_studenta(number)
# zadanie.pobierz_srednia(135792)

#
# class ProductInventory:
#     product_name = ""
#     product_category = ""
#     quantity_available = 0
#     unit_price = 0.0
#
#     def addProduct(self, product_name, product_category, quantity_available, unit_price):
#         self.product_name = product_name
#         self.product_category = product_category
#         self.quantity_available = quantity_available
#         self.unit_price = unit_price
#
#     def showInventory(self):
#         if self.quantity_available > 0:
#             print(f"{self.product_name}, {self.product_category}, {self.quantity_available}, {self.unit_price}")
#         else:
#             pass
#     def sellProduct(self, amount):
#         if self.quantity_available - amount > 0:
#             self.quantity_available - amount
#         else:
#             print("value to high")
#
#
# tab = []
# products_data = [
#     ["Laptop", "Elektronika", 10, 2500.00],
#     ["Koszula", "Odzież", 50, 80.00],
#     ["Sok pomarańczowy", "Spożywcze", 20, 5.00],
#     ["Buty sportowe", "Obuwie", 30, 200.00]
# ]
#
# for product in products_data:
#     zadanie = ProductInventory()
#     zadanie.addProduct(*product)
#     tab.append(zadanie)
#
# for product in tab:
#     product.showInventory()
#
# name = input("podaj nazwe")
# for product in tab:
#     if product.product_name == name:
#         product.sellProduct(int(input("podaj ile chcesz sprzedac")))


# Zaimplementuj w języku Python klasę ZarzadzanieStudentami, która będzie zarządzać danymi dotyczącymi studentów na uczelni.
# Klasa ta powinna przechowywać informacje o studentach jako atrybuty klasy.
#
# Każdy student będzie reprezentowany jako instancja klasy Student. Klasa Student powinna zawierać atrybuty imię, nazwisko, nr_indeksu oraz oceny (lista ocen).
#
# Zdefiniuj następujące metody w klasie ZarzadzanieStudentami:
#
# dodaj_studenta(imie, nazwisko, nr_indeksu) - dodaje nowego studenta do listy studentów.
# usun_studenta(nr_indeksu) - usuwa studenta o podanym numerze indeksu z listy studentów.
# dodaj_ocene(nr_indeksu, ocena) - dodaje ocenę dla studenta o podanym numerze indeksu do listy ocen.
# pobierz_srednia(nr_indeksu) - zwraca średnią ocen studenta o podanym numerze indeksu.
# pobierz_studenta(nr_indeksu) - zwraca informacje o studencie o podanym numerze indeksu (imię, nazwisko, oceny).
# Upewnij się, że klasa ZarzadzanieStudentami jest odpowiednio zaprojektowana pod kątem hermetyzacji danych i obsługi wyjątków.

class ZarzadzanieStudentami:
    imie = ""
    nazwisko = ""
    nr_indeksu = 0
    oceny = []
    def dodaj_studenta(self, imie, nazwisko, nr_indeksu, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.oceny = oceny

    def usun_studenta(self):
        pass

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        print(self.oceny)
    def pobierz_srednia(self):
        srednia = (sum(self.oceny))/len(self.oceny)
        print(srednia)

    def pobierz_studenta(self):
        print(f"{self.imie}, {self.nazwisko}, {self.nr_indeksu}")


tab1 = []
tab = [
    ["Jan", "Kowalski", 12345, [4, 5, 3]],
    ["Anna", "Nowak", 54321, [3, 4]],
    ["Piotr", "Wiśniewski", 98765, [5, 4, 5, 5]]
]

for student in tab:
    zadanie = ZarzadzanieStudentami()
    zadanie.dodaj_studenta(*student)
    tab1.append(zadanie)

ocena = int(input("podaj ocene"))
indeks = int(input("podaj indeks"))

for x in tab1:
    if x.nr_indeksu == indeks:
        x.dodaj_ocene(ocena)
for x in tab1:
    if x.nr_indeksu == indeks:
        x.pobierz_srednia()
for x in tab1:
    x.pobierz_studenta()