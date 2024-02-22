#2
from tkinter import *
class Restauracja:
    nazwa = ""
    kuchnia = ""
    stoliki = 0
    rezerwacje = 0
    def dodawanie(self,nazwa, kuchnia, stoliki, rezerwacje):
        self.nazwa = nazwa
        self.kuchnia = kuchnia
        self.stoliki= stoliki
        self.rezerwacje = rezerwacje

    def wyswietl(self):
        output.insert(END, f"{self.nazwa},{self.kuchnia},{self.stoliki}, {self.rezerwacje}\n")

    def rezerwacja(self, ilosc):
        if self.rezerwacje + ilosc <=  self.stoliki:
            self.rezerwacje += ilosc
            output.config(bg="green",fg="white")
            output.insert(END,"dodano rezerwacje\n")
        else:
            output.config(bg="red", fg="white")
            output.insert(END,"nie ma tylu wolnych stolikow\n")

    def odwolanie(self, ilosc):
        if self.rezerwacje - ilosc >= 0:
            self.rezerwacje -= ilosc
            output.config(bg="green", fg="white")
            output.insert(END,"odwolano\n")
        else:
            output.config(bg="red", fg="white")
            output.insert(END,"nie mozna tylu odwolac\n")


restauracje = [

    ["La Trattoria", "włoska", 20, 5],

    ["Szechuan Garden", "chińska", 30, 8],

    ["Le Petit Bistro", "francuska", 15, 3],

    ["Taste of India", "indyjska", 25, 6],

    ["El Ranchito", "meksykańska", 10, 2]

]
tab = []
for x in restauracje:
    zadanie = Restauracja()
    zadanie.dodawanie(*x)
    tab.append(zadanie)

def zarezerwuj():
    name = name_entry.get()
    ilosc = int(ilosc_entry.get())
    for x in tab:
        if x.nazwa == name:
            x.rezerwacja(ilosc)
            x.wyswietl()

def odwolaj():
    name = name_entry.get()
    ilosc = int(ilosc_entry.get())
    for x in tab:
        if x.nazwa == name:
            x.odwolanie(ilosc)
            x.wyswietl()

window = Tk()
window.title("menu")
window.geometry("600x330")

naglowek = Label(window, text="Menadżer rezerwacji ",font=("Arial Black", 30), fg="black")
naglowek.pack()
napis = Label(window, text="podaj nazwe restauracji:")
napis.pack()


name_entry = Entry(window)
name_entry.pack()



napis1 = Label(window, text="podaj ilosc stolikow:")
napis1.pack()


ilosc_entry = Entry(window)
ilosc_entry.pack()

przycisk = Button(window, text="zarezerwuj stolik", command=zarezerwuj, bg="green", fg="white")
przycisk.pack(pady=3)

przycisk1 = Button(window, text="odwolaj stolik", command=odwolaj, bg="red", fg="white")
przycisk1.pack(pady=5)

output = Text(window)
output.config(bg="grey")
output.pack()

window.mainloop()
