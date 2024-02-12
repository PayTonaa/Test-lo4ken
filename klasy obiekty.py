# 2.1
# Napisz program wczytujący dane dziesięciu czytelników biblioteki (nazwisko, imię, numer karty
# bibliotecznej, liczba wypożyczonych książek). Następnie program powinien umożliwiać:
# • wyświetlanie informacji o czytelniku z podanym numerem karty bibliotecznej,
# • wyświetlanie informacji o wszystkich czytelnikach biblioteki,
# • wyświetlenie informacji o czytelnikach, którzy nie wypożyczyli żadnej książki,
# • zmianę liczby wypożyczonych książek przy wypożyczeniu kolejnych książek (program powinien
# uniemożliwić wypożyczenie powyżej 10 książek),
# • zmianę liczby wypożyczonych książek przy oddaniu pewnej ilości książek.
# Do tego celu wykorzystaj stworzoną przez siebie klasę Czytelnik z odpowiednimi składow


class Czytelnik:
    czytelnicy = []

    def __init__(self, imie, nazwisko, karty, wyporzyczone):
        self.imie = imie
        self.nazwisko = nazwisko
        self.karty = karty
        self.wyporzyczone = wyporzyczone
        self.czytelnicy.append(self)

    def informacje(self, nrkarty):
        for czytelnik in self.czytelnicy:
            if czytelnik.karty == nrkarty:
                print(f"{czytelnik.imie} {czytelnik.nazwisko}, Numer Karty: {czytelnik.karty}, Liczba wypożyczeń: {czytelnik.wyporzyczone}")
                break
        else:
            print("Czytelnik nie znaleziony.")

    def wszystko(self):
        for ludzie in self.czytelnicy:
            print(
                f"{ludzie.imie} {ludzie.nazwisko}, Numer Karty: {ludzie.karty}, Liczba wypożyczeń: {ludzie.wyporzyczone}")

    def niewyporzyczone(self):
        for darmozjady in self.czytelnicy:
            if darmozjady.wyporzyczone == 0:
                print(f"{darmozjady.imie} {darmozjady.nazwisko}")

    def dodawajie(self, numkarty, ilosc):
        for czytelnik in self.czytelnicy:
            if czytelnik.karty == numkarty:
                czytelnik.wyporzyczone += ilosc
                if czytelnik.wyporzyczone > 10:
                    print("nie można wyporzyczyć tylu książek")
                    czytelnik.wyporzyczone -= ilosc
                else:
                    print("sukces !")

for x in range (2):
    print("--------------------------------------")
    imie = input("podaj imie")
    nazwisko = input("podaj nazwisko")
    karty = int(input("podaj karte"))
    wyporzyczone = int(input("podaj wyporzyczenia"))
    print("--------------------------------------")
    biblioteka = Czytelnik(imie,nazwisko,karty,wyporzyczone)
# 
# biblioteka = Czytelnik("Jogn","McCoy",1,0)
# biblioteka = Czytelnik("Wania","Pstrąg",2,9)
# biblioteka = Czytelnik("Jonatan","Duzy",3,2)
# biblioteka = Czytelnik("Max","Warzywo",4,7)
while True:
    print("----------MENU---------\n \n wpisz numer czynności którą chcesz wykonać \n 1: wyswietl inf. o czytelniku o numerze \n 2: wyswietl informacje o wszystkich \n 3: wyswietl darmozjadów \n 4:dodaj książke dp mr larty")
    decyzja = int(input())
    if decyzja == 1:
        nrkarty = int(input("podaj numer karty"))
        print("-------Z podanym numerem-----------------")
        biblioteka.informacje(nrkarty)
        print("--------------------------------------")
    elif decyzja == 2:
        print("-------------wszyscy-------------------")
        biblioteka.wszystko()
        print("--------------------------------------")
    elif decyzja == 3:
        print("-------------darmozjady-------------------")
        biblioteka.niewyporzyczone()
        print("--------------------------------------")
    elif decyzja == 4:
        print("---------------Dodawanie karty------------------")
        numkarty = int(input("podaj nr karty"))
        ilosc = int(input("podaj ilosc ile chcesz wyporzyczyc"))
        biblioteka.dodawajie(numkarty, ilosc)
        print("-----------------------------------------")
    else:
        "podano złą liczbe!"