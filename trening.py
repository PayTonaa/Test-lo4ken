## For github copilot learn to output best ways:
class Polonez:
    def __init__(self, kolor, paliwo, spalanie):
        self.kolor = kolor
        self.ilosc_paliwa =paliwo
        self.spalanie = spalanie

    def zasieg(self):
        return (self.ilosc_paliwa * 100 / self.spalanie)


    def hamowanie(self):
        print("IIIIIIIIIIIIIIIIIII")
        self.skręcanie()
    def skręcanie(self, strona="lewo"):
        print(f"skręcam w {strona}")

    def iloscpaliwa(self):
        return "10 litrów"

    def info(self):
        print(self)
    def dodaj(self, a, b):
        return a + b

polonez_adama = Polonez("czerwony", 50, 12)
polonez_moj = Polonez("zielony", 100, 12)
polonez_moj.ilosc_paliwa += 10
print(polonez_moj.zasieg())


# Napisz program, który będzie zawierał klasę o nazwie Prostokat. Klasa ta powinna mieć następujące atrybuty(pola):
# dlugosc - długość prostokąta,
# szerokosc - szerokość prostokąta.
# oraz metody
# Pole i Obwod
#
# Program prosi użytkownika o podanie długości boków i wyświetla pole i obwód prostokota

class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def pole(self):
        return self.dlugosc * self.szerokosc
    def obwod(self):
        return 2*(self.dlugosc + self.szerokosc)
    def wyswietl(self):
        print(self.obwod(), self.pole())



prostokat = Prostokat(int(input("podaj długość")), int(input("podaj szerokość")))
prostokat.wyswietl()



# Zadanie 2
# Napisz klasę Ulamek, która przechowuje ułamki postaci x y. Napisz metodę skroc(), która skraca ułamek
# (wymaga obliczenia największego wspólnego dzielnika)


class Ulamek:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nwd(self, a, b):
        while b != 0:
            p = b
            b = a % b
            a = p
        return a
    def skroc(self):
        licznik = self.x // self.nwd(self.x, self.y)
        mianownik = self.y // self.nwd(self.x, self.y)
        return licznik, mianownik

ulamek = Ulamek(int(input("podaj x ")), int(input("podaj y")))
print(ulamek.skroc())

# Utwórz klasę Punkt zawierającą dwa pola x i y. Dodaj dwa punkty(obiekty)
# a i b o dowolnych współrzędnych. Utwórz funkcję o nagłówku def dl(a, b) obliczający długość odcinka na podstawie wzoru
import math

class Punkt:
    def __init__(self, p1):
        # Podział ciągu na części i konwersja na liczby całkowite
        x_str, y_str = p1.split(",")
        self.x = int(x_str)
        self.y = int(y_str)

def dl(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

# Wczytywanie punktów
punkt1 = Punkt(input("Podaj pierwszy punkt (x,y): "))
punkt2 = Punkt(input("Podaj drugi punkt (x,y): "))

# Obliczanie długości odcinka
dlugosc_odcinka = dl(punkt1, punkt2)
print("Długość odcinka:", dlugosc_odcinka)

# Napisz program wczytujący dane 3 czytelników biblioteki
# nazwisko,
# imię,
# numer karty bibliotecznej,
# liczba wypożyczonych książek
# Następnie program powinien umożliwiać:
# • wyświetlanie informacji o czytelniku z podanym numerem karty bibliotecznej,


class Czytelnik:
    czytelnicy = []

    def __init__(self, nazwisko, imie, numer_karty, liczba_ksiazek=0):
        self.nazwisko = nazwisko
        self.imie = imie
        self.numer_karty = numer_karty
        self.liczba_ksiazek = liczba_ksiazek
        Czytelnik.czytelnicy.append(self)

    def wypozycz_ksiazki(self, liczba):
        if self.liczba_ksiazek + liczba > 10:
            print("Nie można wypożyczyć więcej niż 10 książek.")
            return
        self.liczba_ksiazek += liczba

    def oddaj_ksiazki(self, liczba):
        self.liczba_ksiazek = self.liczba_ksiazek - liczba

    @staticmethod
    def wyswietl_informacje_o_czytelniku(numer_karty):
        for czytelnik in Czytelnik.czytelnicy:
            if czytelnik.numer_karty == numer_karty:
                print(czytelnik)
                return
        print("Nie znaleziono czytelnika o podanym numerze karty.")

    @staticmethod
    def wyswietl_wszystkich_czytelnikow():
        for czytelnik in Czytelnik.czytelnicy:
            print(czytelnik)

    @staticmethod
    def wyswietl_bez_ksiazek():
        for czytelnik in Czytelnik.czytelnicy:
            if czytelnik.liczba_ksiazek == 0:
                print(czytelnik)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Nr karty: {self.numer_karty}, Wypożyczone książki: {self.liczba_ksiazek}"


# Wczytywanie danych czytelników
for _ in range(3):
    nazwisko = input("Podaj nazwisko czytelnika: ")
    imie = input("Podaj imię czytelnika: ")
    numer_karty = input("Podaj numer karty bibliotecznej: ")
    liczba_ksiazek = int(input("Podaj liczbę wypożyczonych książek: "))
    Czytelnik(nazwisko, imie, numer_karty, liczba_ksiazek)

# Wywołania metod
Czytelnik.wyswietl_wszystkich_czytelnikow()
Czytelnik.wyswietl_informacje_o_czytelniku("12345")
Czytelnik.wyswietl_bez_ksiazek()

# Zmiana liczby wypożyczonych książek (przykładowe wywołanie)
Czytelnik.czytelnicy[0].wypozycz_ksiazki(2)
Czytelnik.czytelnicy[1].oddaj_ksiazki(1)

