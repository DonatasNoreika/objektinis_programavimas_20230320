
class Irasas:
    def __init__(self, suma, tipas):
        self.suma = suma
        self.tipas = tipas

    def __str__(self):
        return f"{self.tipas}: {self.suma}"


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        irasas = Irasas(suma, "Pajamos")
        self.zurnalas.append(irasas)

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)


biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - pridėti pajamas\n4 - ataskaita\n0 - išeiti\n"))
    match pasirinkimas:
        case 1:
            suma = float(input("Suma: "))
            biudzetas.prideti_pajamu_irasa(suma)
        case 4:
            biudzetas.parodyti_ataskaita()
        case 0:
            print("Viso gero")
            break
