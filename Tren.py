from Engranaje import Engranaje
from decimal import Decimal

class Tren:
    def __init__(self, conductor, conducido):
        self.conductor = conductor
        self.conducido = conducido

    def setTren(self, conductor, conducido):
        self.conductor = conductor
        self.conducido = conducido

    def getTren(self):
        return(self.conductor, self.conducido)

    def distanciaCentros(self):
        return((self.conductor.diametroPrimitivo()+self.conducido.diametroPrimitivo())/2)

e1 = Engranaje(2,20,20)
e2 = Engranaje(2,10,20)
tren1 = Tren(e1,e2)
print(e1)
print(f"Distancia entre centros: {Decimal(tren1.distanciaCentros())}")
