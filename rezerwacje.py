from tkinter import *
class Restauracja:
    nazwa = ""
    kuchnia = ""
    ilosc_stolikow = 0
    ilosc_rezerwacji = 0


    def nowe(self, nazwa, kuchnia, ilosc_stolikow, ilosc_rezerwacji):
        self.nazwa = nazwa
        self.kuchnia = kuchnia
        self.ilosc_stolikow = ilosc_stolikow
        self.ilosc_rezerwacji = ilosc_rezerwacji

    def wyswietlanie(self):
        tekscior.insert(END, f"{self.nazwa}, {self.kuchnia}, {self.ilosc_rezerwacji}, {self.ilosc_stolikow} \n")

    def rezerwacja(self, ilosc):
        if self.ilosc_rezerwacji + ilosc <= self.ilosc_stolikow:
            self.ilosc_rezerwacji += ilosc
            tekscior.config(bg="green")
            tekscior.insert(END,"wykonano rezerwacje \n")
        else:
            tekscior.config(bg="red")
            tekscior.insert(END,"nine ma tylu wolnych stolików \n")

    def odwolanie(self, ilosc):
        if self.ilosc_rezerwacji - ilosc < 0:
            tekscior.config(bg="red")
            tekscior.insert(END,"nie mozesz iec tylu rezerwacji \n")
        else:
            self.ilosc_rezerwacji -= ilosc
            tekscior.config(bg="green")
            tekscior.insert(END,"odwolano rezerwacje \n")

restauracje = [

    ["La Trattoria", "włoska", 20, 5],
    ["Szechuan Garden", "chińska", 30, 8],
    ["Le Petit Bistro", "francuska", 15, 3],
    ["Taste of India", "indyjska", 25, 6],
    ["El Ranchito", "meksykańska", 10, 2]

]
restauracja = []
for rest in restauracje:
    zadanie = Restauracja()
    zadanie.nowe(*rest)
    restauracja.append(zadanie)

def rezerwacja():
    nazwa = nazwa_entry.get()
    ilosc = int(ilosc_entry.get())
    for rest in restauracja:
        if rest.nazwa == nazwa:
            rest.rezerwacja(ilosc)
            rest.wyswietlanie()

def odwolanie():
    nazwa = nazwa_entry.get()
    ilosc = int(ilosc_entry.get())
    for rest in restauracja:
        if rest.nazwa == nazwa:
            rest.odwolanie(ilosc)
            rest.wyswietlanie()

window = Tk()
window.title("restauracje")
window.geometry("540x450")

naglowek = Label(window, text="MENADŻER REZERWACJI", font=("Arial Black", 20), pady=30)
naglowek.pack()
tekst = Label(window, text="podaj nazwe restauracji")
tekst.pack()

nazwa_entry = Entry(window)
nazwa_entry.pack()


tekst1 = Label(window, text="podaj ilosc miejsc")
tekst1.pack()

ilosc_entry = Entry(window)
ilosc_entry.pack()

przycisk = Button(window, text="zarezerwuj miejsce", command=rezerwacja, bg="green", fg="white")
przycisk.pack(pady = 3)

przycisk1 = Button(window, text="odwolaj miejsce", command=odwolanie, bg="red", fg="white")
przycisk1.pack(pady = 8)

tekscior = Text(window)
tekscior.config(bg="grey", fg="white")
tekscior.pack()

window.mainloop()
