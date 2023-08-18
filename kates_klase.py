class Kate:
    def __init__(self, spalva, vardas='Murksė', kojos=4):
        self.spalva = spalva
        self.kojos = kojos
        self.vardas = vardas

    def miaukseti(self, zinute='Miau', kiekis=1):
        print(zinute * kiekis)
        print(self.vardas)

    def __str__(self):
        # return f'Hello, mes pirmą kartą pakeitėme ką Python printins' (pakeis veiškų printą į mūsų norimą stringą
        return f"Hello, mano vardas {self.vardas}, spalva {self.spalva}"

    def __repr__(self):  # Magic metodas , kad spausdintų listuose
        return f" {self.vardas}|{self.spalva}|{self.kojos}"