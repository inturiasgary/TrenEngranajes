import math
from math import radians


class Engranaje:
    def __init__(self, z, modulo, anguloHelice=0):
        self.z = z
        self.modulo = modulo
        self.anguloHelice = anguloHelice

    def diametroPrimitivo(self):
        return (self.z*self.modulo/math.cos(radians(self.anguloHelice)))

    def diametroExterior(self):
        return (self.diametroPrimitivo()+(2*self.modulo))

    def diametroInterior(self):
        return (self.diametroExterior()-(2*2.25*self.modulo))
