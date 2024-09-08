import math
from math import radians
from Engranaje import Engranaje
from decimal import Decimal

class Maquina:
    def __init__(self, constanteCinetica, engranajeRequerido):
        self.constanteCinetica = constanteCinetica
        self.engranajeRequerido = engranajeRequerido

    def pasoHelice(self):
        pass

    def diferencial(self):
        return(self.constanteCinetica*math.sin(radians(self.engranajeRequerido.anguloHelice))/self.engranajeRequerido.modulo)

e1 = Engranaje(20,2,30.5)
m1 = Maquina(9, e1)
print(m1.engranajeRequerido.diametroExterior())
print(Decimal(m1.diferencial()))

print(round(math.sin(radians(e1.anguloHelice)),10))