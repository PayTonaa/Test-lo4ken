from tkinter import *

class Bank:
    numer_konta = ""
    saldo = 0.0
    właściciel_konta = ""
    typ_konta = ""
    def dodawanie(self, numer_konta, saldo , właściciel_konta, typ_konta):
        self.numer_konta = numer_konta
        self.saldo = saldo
        self.właściciel_konta = właściciel_konta
        self.typ_konta = typ_konta

    def wyswietl(self):
        tekscior.insert(END, f"{self.numer_konta}, {self.właściciel_konta}, {self.saldo}, {self.typ_konta} \n")


    def wpłacanie(self, value):
        self.saldo += value
        tekscior.config(bg="green", fg="white")
        tekscior.insert(END,f"wpłacono {value} \n")

    def wyplacanie(self, value):
        if self.saldo - value >= 0:
            self.saldo -= value
            tekscior.config(bg="orange", fg="white")
            tekscior.insert(END,"wyplacono srodi \n")
        else:
            tekscior.config(bg="red", fg="white")
            tekscior.insert(END,"za mało środków \n")

konta_bankowe = [
    ["123456789", 1500.50, "Jan Kowalski", "oszczędnościowe"],

    ["987654321", 3000.0, "Anna Nowak", "rozliczeniowe"],

    ["111222333", 500.75, "Katarzyna Nowak", "oszczędnościowe"],

    ["444555666", 2000.0, "Piotr Wiśniewski", "rozliczeniowe"],

    ["777888999", 10000.0, "Alicja Kowalczyk", "oszczędnościowe"]
]
konta = []

def dodawanie():
    number = konto_entry.get()
    value = float(wartosc_entry.get())
    for x in konta:
        if x.numer_konta == number:
            x.wpłacanie(value)
            x.wyswietl()

def wyplacanie():
    number = konto_entry.get()
    value = float(wartosc_entry.get())
    for x in konta:
        if x.numer_konta == number:
            x.wyplacanie(value)
            x.wyswietl()

for x in konta_bankowe:
    zadnaie = Bank()
    zadnaie.dodawanie(*x)
    konta.append(zadnaie)

window = Tk()
window.title("Bank")
window.geometry("500x350")

informacja = Label(window, text="Zarządzaj swoim kontem!", font = ('Arial', 30, 'bold'))
informacja.pack()
tekst = Label(window, text="podaj numer konta")
tekst.pack()

konto_entry = Entry(window)
konto_entry.pack()

tekst1 =tekst = Label(window, text="podaj wartosc")
tekst1.pack()

wartosc_entry = Entry(window)
wartosc_entry.pack()


przycisk = Button(window, text="wplac pieniądze", command=dodawanie, bg="green", fg="white")
przycisk.pack(pady = 3)

przycisk1 = Button(window, text="wyplac pieniądze", command=wyplacanie, bg="red", fg="white")
przycisk1.pack(pady = 3)

tekscior = Text(window)
tekscior.config(bg="grey", fg="green")
tekscior.pack()

window.mainloop()
