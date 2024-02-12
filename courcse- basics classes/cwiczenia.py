# Napisz program wczytujący dane dziesięciu czytelników biblioteki (nazwisko, imię, numer karty
# bibliotecznej, liczba wypożyczonych książek). Następnie program powinien umożliwiać:
# • wyświetlanie informacji o czytelniku z podanym numerem karty bibliotecznej,
# • wyświetlanie informacji o wszystkich czytelnikach biblioteki,
# • wyświetlenie informacji o czytelnikach, którzy nie wypożyczyli żadnej książki,
# • zmianę liczby wypożyczonych książek przy wypożyczeniu kolejnych książek (program powinien
# uniemożliwić wypożyczenie powyżej 10 książek),
# • zmianę liczby wypożyczonych książek przy oddaniu pewnej ilości książek.
# Do tego celu wykorzystaj stworzoną przez siebie klasę Czytelnik z odpowiednimi składowymi.


# class Biblioteka:
#     def __init__(self, imie, nazwisko, nrkarty, liczbawyp):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.nrkarty = nrkarty
#         self.liczbawyp = liczbawyp

#     def podanynumer(self, numer):
#         if self.nrkarty == numer:
#             print(f"{self.imie}, {self.nazwisko}")

#     def wszyscy(self):
#         print(f"{self.imie}, {self.nazwisko}, {self.nrkarty}, {self.liczbawyp}")

#     def darmozjady(self):
#         if self.liczbawyp == 0:
#             print(f"{self.imie}, {self.nazwisko}")

#     def szukanie(self, imie, ilosc):
#         if self.nrkarty == imie:
#             self.liczbawyp += ilosc
#             if self.liczbawyp > 10:
#                 print("nie można tyle wypożyczyć")
#             else:
#                 print("miłego czytania")


# czytelnicy = [
#     Biblioteka("Jonatan", "Pstrąg", "001", 0),
#     Biblioteka("Maks", "Sporekule", "002", 2),
#     Biblioteka("Warzywo", "Kasiuba", "003", 9),
#     Biblioteka("Max", "Hulajnoga", "004", 0)
# ]


# numer = input("podaj numer karty")
# for czyelnik in czytelnicy:
#     czyelnik.podanynumer(numer)

# print("wszyscy użytkownicy biblioteki")
# for wszyscy in czytelnicy:
#     wszyscy.wszyscy()

# print("darmozjady:")
# for darmozjady in czytelnicy:
#     darmozjady.darmozjady()

# identyfikator = input("podaj identyfikator do kogo chcesz dodac książke")
# ilosc = int(input("podaj ilość książek do wypożyczenia"))
# for ludzie in czytelnicy:
#     ludzie.szukanie(identyfikator, ilosc)


########################
# Zapłata za dobę hotelową wynosi 50 złotych, jeżeli pobyt w hotelu był dłuższy niż 7 dni,
# 75 złotych dla pobytu od 4 do 7 dni oraz 100 zł dla pobytu krótszego niż 4 doby. Napisz
# program, który dla wczytanej od użytkownika liczby dób hotelowych, obliczy i wyświetli
# informację o opłacie za podaną liczbę dób.


# class Hotel:
#     def __init__(self, imie, dlugosc):
#         self.dlugosc = dlugosc
#         self.imie = imie

#     def zaplata(self):
#         if self.dlugosc <= 4:
#             print ( "do zaplaty", self.dlugosc * 100)
#         elif self.dlugosc > 4 and self.dlugosc <= 7:
#             print ( "do zaplaty", self.dlugosc * 75)
#         elif self.dlugosc > 7:
#             print ( "do zaplaty", self.dlugosc * 50)


# doby = [
#     Hotel("Pietrzykowski", 12),
#     Hotel("Warzywko",1),
#     Hotel("Śmietnik", 22),
#     Hotel("Kasztanek", 5)
# ]

# for rezerwacje in doby:
#     rezerwacje.zaplata()


# Napisz program wczytujący dane dziesięciu czytelników biblioteki (nazwisko, imię, numer karty
# bibliotecznej, liczba wypożyczonych książek). Następnie program powinien umożliwiać:
# • wyświetlanie informacji o czytelniku z podanym numerem karty bibliotecznej,
# • wyświetlanie informacji o wszystkich czytelnikach biblioteki,
# • wyświetlenie informacji o czytelnikach, którzy nie wypożyczyli żadnej książki,
# • zmianę liczby wypożyczonych książek przy wypożyczeniu kolejnych książek (program powinien
# uniemożliwić wypożyczenie powyżej 10 książek),
# • zmianę liczby wypożyczonych książek przy oddaniu pewnej ilości książek.
# Do tego celu wykorzystaj stworzoną przez siebie klasę Czytelnik z odpowiednimi składowymi.


# class Biblioteka:
#     czlonkowie = []

#     def __init__(self, imie, nazwisko, numerkarty, liczba):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.numerkarty = numerkarty
#         self.liczba = liczba
#         Biblioteka.czlonkowie.append(self)

#     def podanynumer(self, numer):
#         for czlonkowie in self.czlonkowie:
#             if numer == czlonkowie.numerkarty:
#                 print(f"{self.imie}, {self.nazwisko}")

#     def wszyscy(self):
#         for wszyscy in self.czlonkowie:
#             print(f"{wszyscy.imie}, {wszyscy.nazwisko}, {wszyscy.numerkarty}")

#     def darmozjadfy(self):
#         for darmozjady in self.czlonkowie:
#             if darmozjady.liczba == 0:
#                 print(f"{self.imie}, {self.nazwisko}")

#     def zmiania(self, numer, liczba):
#         for zmiania in self.czlonkowie:
#             if zmiania.numerkarty == numer:
#                 zmiania.liczba += liczba
#                 if liczba > 10:
#                     print("nie mozna tylu ksiazek")
#                     zmiania.liczba -= liczba
#                 else:
#                     print("succes")


# for x in range(3):
#     imie = input("podaj imie")
#     nazwisko = input("podaj nazwisko")
#     numerekarty = int(input("Podaj nr karty"))
#     liczenieksz = int(input("Ile książek wypożyczy"))
#     Biblioteka(imie, nazwisko, numerekarty, liczenieksz)

# nuemr = int(inpup("podaj numer karty bibliotecznej"))
# liczba = int(input("podaj lkczbe "))


# Stwórz klasę na nazwie Zwierze dodaj atrybuty takie jak imie, gatunek i wiek, płeć Następnie utwórz kilka obiektów tej klasy w tablicy reprezentujących rózenie zwierzęta takie jak pies kot i ryba
# Utwórz metodę wyświetlającą wszystkie informacje o zwierzęciu
# Wyświetl wszystkie zwierzęta płci męskiej
# wyświetrl zwierzę na podtawie podnaego imienia


# class Zwierze:
#     def __init__(self, imie, gatunek, wiek, plec):
#         self.imie = imie
#         self.gatunek = gatunek
#         self.wiek = wiek
#         self.plec = plec

#     def wszystko(self):
#         print(f"{self.imie}, {self.gatunek}, {self.wiek} lat, {self.plec}")

#     def men(self):
#         if self.plec == "m":
#             self.wszystko()

#     def poimieniu(self, imie):
#         if self.imie == imie:
#             self.wszystko()


# zwierzeta = [
#     Zwierze("Azor", "Pies", 12, "m"),
#     Zwierze("Kicia", "Kot", 12, "m"),
#     Zwierze("Glupik", "Ryba", 1, "k"),
# ]
# main = "============================"
# print(main)
# for atr in zwierzeta:
#     atr.wszystko()
# print(main)
# for zwierzaki in zwierzeta:
#     zwierzaki.men()
# print(main)
# imie = input("podaj imie:")
# for zwierzaki in zwierzeta:
#     zwierzaki.poimieniu(imie)


# Stwórz klasę na nazwie Zwierze dodaj atrybuty takie jak imie, gatunek i wiek, płeć Następnie utwórz kilka obiektów tej klasy w tablicy reprezentujących rózenie zwierzęta takie jak pies kot i ryba
# Utwórz metodę wyświetlającą wszystkie informacje o zwierzęciu
# Wyświetl wszystkie zwierzęta płci męskiej
# wyświetrl zwierzę na podtawie podnaego imienia


# class Zwierze:
#     def __init__(self, imie, gatunek, wiek, plec):
#         self.imie = imie
#         self.gatunek = gatunek
#         self.wiek = wiek
#         self.plec = plec

#     def wyswietl(self):
#         print(f"{self.imie}, {self.gatunek}, {self.wiek}, {self.plec}")

#     def meska(self):
#         if self.plec == "m":
#             self.wyswietl()

#     def named(self, imie):
#         if self.imie == imie:
#             self.wyswietl()


# Zwierzeta = [
#     Zwierze("Burek", "Pied", 12, "m"),
#     Zwierze("Katze", "Kot", 2, "m"),
#     Zwierze("LeFishe", "Ryba", 1, "k"),
]

main = "================================"
print(main)
for animals in Zwierzeta:
    animals.wyswietl()
print(main)
for animals in Zwierzeta:
    animals.meska()
print(main)
imie = input("Podaj imię zwierzęcia: ")
for animals in Zwierzeta:
    animals.named(imie)

Zadanie 4
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu ax2+bx+c. Klasa powinna zawierać trzy pola:
a, b, c,
które są przypisywane w konstruktorze.
Główną metodą powinna być ObliczKw(), która zwraca miejsca zerowe podanej funkcji.
Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0, a także obmyślić sposób informowania o nieskończonej liczbie, jednym rozwiązaniu lub brak rozwiązań.

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ObliczkKw(self):
        roz = self.b ** 2 - (4*self.a * self.c)
        if roz < 0:
            return "Nie ma roz"
        elif roz == 0:
            x = -self.b/2 * self.a
            return x
        elif roz > 0: 
            x1 = (-self.b + roz) / 2 * self.a
            x2 = (-self.b - roz) / 2 * self.a
            return x1, x2


a = 1
b = 4
c = 2
funkcja = FunkcjaKwadratowa(a, b, c)
print(funkcja.ObliczkKw())
                                    