class Audi:
    def __init__(self, kolor, kondycja):
        self.kolor  = kolor
        self.ilosc_paliwa = 10
        self.kondycja = kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.maksymalna_predkosc = 100
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
           self.maksymalna_predkosc = 50
           print("tryb eco")
       elif self.tryb == "normal":
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            self.maksymalna_predkosc = 100
            print("tryb normal")
       else:
           print("tryb nierozpoznany")
    def wlacz_eco(self):
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = True
        self.maksymalna_predkosc = 50
        print("tryb eco wlaczony")
    def wlacz_normal(self):
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        self.maksymalna_predkosc = 100
        print("tryb normal wlaczony")
    def tankowanie(self, litr):
        if self.ilosc_paliwa + litr > 70:
            print("za duzo")
        elif litr < 5:
            print("tyle sie nie da")
        else:
            self.ilosc_paliwa += round(litr)
            print(f"zatankowalem i mam {self.ilosc_paliwa} ")



moje_auto = Audi("czerwony", 4)
auto_sasiada = Audi("zielony", 5)


print(moje_auto.wlacz_normal())
print(moje_auto.zasieg())
print(moje_auto.tankowanie(17))
