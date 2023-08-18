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


kate1_obj = Kate('Juoda')
print(kate1_obj)

print(kate1_obj.spalva)
kate1_obj.spalva = 'raina'
print(kate1_obj)

kate2_obj = Kate("balta", vardas="Albinosė")
print(kate2_obj)

kate3_obj = Kate("ruda", vardas="Rudė")
print(kate3_obj)
kate3_obj.vardas = "Ryžė"
print(kate3_obj)

kaciu_listas = [kate1_obj, kate2_obj, kate3_obj]  # sudedam į listą kates
print(kaciu_listas)

print('--------------')

for kate_obj in kaciu_listas:
    #  print(kate_obj.vardas, kate_obj.spalva)
    if kate_obj.spalva == 'balta':
        print('Baltos kaitės vardas', kate_obj.vardas)
        kate_obj.vardas = 'Meška'

print(kaciu_listas)