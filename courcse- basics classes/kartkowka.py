# Stwórz klasę na nazwie Zwierze dodaj atrybuty takie jak imie, gatunek i wiek, płeć Następnie
class Zwierze:
    def __init__(self, imie, gatunek, wiek, plec):
        self.imie = imie
        self.gatunek = gatunek
        self.wiek = wiek
        self.plec = plec

    # Utwórz metodę wyświetlającą wszystkie informacje o zwierzęciu
    def wyswietl(self):
        print(f'Imie: {self.imie}, Gatunek: {self.gatunek}, Wiek: {self.wiek}, Płeć: {self.plec}')

    # Wyświetl wszystkie zwierzęta płci męskiej
    def wyswietl_m(self):
        if self.plec == 'm':
            self.wyswietl()

    # wyświetrl zwierzę na podtawie podnaego imienia
    def wyswietl_imie(self, imie):
        if self.imie == imie:
            self.wyswietl()


# utwórz kilka obiektów tej klasy w tablicy reprezentujących rózenie zwierzęta takie jak pies kot i ryba
zwierzeta = [
    Zwierze('Burek', 'pies', 5, 'm'),
    Zwierze('Reksio', 'pies', 3, 'm'),
    Zwierze('Filemon', 'kot', 2, 'm'),
    Zwierze('Kajtek', 'kot', 1, 'm'),
    Zwierze('Złota rybka', 'ryba', 1, 'k'),
]

# wyświetl wszystkie zwierzęta
print('Wszystkie zwierzęta:')
for zwierze in zwierzeta:
    zwierze.wyswietl()

# wyświetl wszystkie zwierzęta płci męskiej
print('Wszystkie zwierzęta płci męskiej:')
for zwierze in zwierzeta:
    zwierze.wyswietl_m()

# wyświetl zwierzę na podtawie podnaego imienia
print('Zwierzę o imieniu Reksio:')
for zwierze in zwierzeta:
    zwierze.wyswietl_imie('Reksio')