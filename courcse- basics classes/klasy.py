class Ulamek:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Pokaz(self):
        print(self.x )
        print(self.y)

    def nwd(self, a, b):
        while b != 0:
            p = b
            b = a % b
            a = p
        return a

    def Skroc(self):
        n = self.nwd(self.x, self.y)
        self.x = self.x // n
        self.y = self.y // n


u1 = Ulamek(20, 24)
u1.Skroc()
u1.Pokaz()