import tkinter as tk
import random

class SzekspirBanner(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Szekspir Banner")
        self.geometry("400x200")

        self.label = tk.Label(self, text="", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.update_banner()

    def update_banner(self):
        szekspir_cytaty = [
            "To be or not to be, that is the question.",
            "All the world's a stage, and all the men and women merely players.",
            "Love all, trust a few, do wrong to none.",
            "The better part of Valour, is Discretion.",
            "All that glisters is not gold.",
            "If music be the food of love, play on.",
        ]

        losowy_cytat = random.choice(szekspir_cytaty)
        self.label.config(text=losowy_cytat)

        self.after(5000, self.update_banner)  # Aktualizuj co 5000 milisekund (5 sekund)

if __name__ == "__main__":
    app = SzekspirBanner()
    app.mainloop()
