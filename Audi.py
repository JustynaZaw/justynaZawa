class Audi:
    def __init__(self, kolor, kondycja):
        self.kolor  = kolor
        self.ilosc_paliwa = 10
        self.kondycja = kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
    def __str__(self):
        napis = (f"Audi ma kolor {self.kolor} i jest w kondycji {self.kondycja}")
        return napis
    def zasieg(self):
        zasieg  = self.ilosc_paliwa / self.spalanie_na_100 * 100
        return round(zasieg)
    def ustaw_tryb(self, tryb):
       self.tryb = tryb
       if self.tryb == "eco":
            self.spalanie_na_100 = 10
            self.tryb_ekonomiczny = True
            print("tryb eco")
       elif self.tryb == "normal":
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            print("tryb normal")
       else:
           print("tryb nierozpoznany")
    def wlacz_eco(self):
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = True
        print("tryb eco wlaczony")
    def wlacz_normal(self):
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        print("tryb normal wlaczony")


moje_auto = Audi("czerwony", 4)
auto_sasiada = Audi("zielony", 5)


print(moje_auto.ustaw_tryb("eco"))
