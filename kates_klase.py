class Kate:
    def __init__(self, spalva, vardas='Murksė', kojos=4):
        self.spalva = spalva
        self.kojos = kojos
        self.vardas = vardas

    def miaukseti(self, zinute='Miau', kiekis=1):
        print(zinute * kiekis)
        print(self.vardas)
