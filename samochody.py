# Napisz program wczytujący dane pięciu samochodów (marka pojazdu, pojemność silnika, rok pro-
# dukcji, numer rejestracyjny, nazwisko właściciela). Następnie program powinien umożliwiać:
# • wyświetlanie informacji o samochodzie z podanym numerem rejestracyjnym,
# • wyświetlanie informacji o wszystkich samochodach,
# • zmianę właściciela pojazdu o podanym numerze rejestracyjnym,
# • wyświetlenie informacji o pojazdach wyprodukowanych przed podanym rokiem,
# • posortowanie pojazdów względem pojemności silnika (od najmniejszej do największej).
# Do tego celu wykorzystaj stworzoną przez siebie klasę Samochód z odpowiednimi składowymi.

class Samochod:
    def __init__(self, marka, model, rocznik,rejestracja,wlascicel, pojemnosc):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.rejestracja = rejestracja
        self.wlasciciel = wlascicel
        self.pojemnosc = pojemnosc

    @staticmethod
    def informacje(rejestracja, samochody):
        for auto in samochody:
            if auto.rejestracja == rejestracja:
                print(f"{auto.marka}, {auto.model}, {auto.rocznik}, {auto.wlasciciel}")
                break

    @staticmethod
    def wszystkie(samochody):
        for samochod in samochody:
            print(f"{samochod.marka}, {samochod.model}, {samochod.rocznik}, {samochod.wlasciciel}, {samochod.rejestracja}")

    @staticmethod
    def zmiana(samochody, nowy, rejestracaj):
        for sprzedarz in samochody:
            if sprzedarz.rejestracja == rejestracaj:
                sprzedarz.wlasciciel = nowy
                print(f"{sprzedarz.marka}, {sprzedarz.wlasciciel}, {sprzedarz.rejestracja}")

    @staticmethod
    def roczniki(rok, samochody):
        for auta in samochody:
            if auta.rocznik == rok:
                print(f"{auta.model}, {auta.marka}")
    @staticmethod
    def srotowanie(samochody):
        for pojemnosci in samochody:
            pojemnosci.pojemnosc.sort()

            

# for dane in range(5):
#     marka = input("podaj markę pojazdu: ")
#     pojemnosc = int(input("podaj pojemnosc silnika: "))
#     rocznik = int(input("podaj rocznik samochodu: "))
#     rejestracja = input("podaj numer rejestracyjny")
#     wlasciciel = input("podaj nazwisko własciciela")
#     dane = Samochod(marka, pojemnosc, rocznik, rejestracja, wlasciciel)
samochody = [
    Samochod("Ford", "Cmax", 2014, "SB7597L", "Grzanka", 1998),
    Samochod("Audi", "A5", 2019, "SK1234K", "Warzywo", 1000),
    Samochod("Ford", "Focus", 2004, "RZ0597L", "Rower", 1500),
]

Samochod.informacje("SB7597L", samochody)
Samochod.wszystkie(samochody)
Samochod.zmiana(samochody, "Rak", "SB7597L")
Samochod.roczniki(2014, samochody)
