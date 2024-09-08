import math
from math import radians

class Engranaje:
    def __init__(self,z ,modulo, anguloHelice = 0):
        self.z = z
        self.modulo = modulo
        self.anguloHelice = anguloHelice

    def diametroPrimitivo(self):
        return (self.z*self.modulo/math.cos(radians(self.anguloHelice)))
       
    def diametroExterior(self):
        return (self.diametroPrimitivo()+(2*self.modulo))
    
    def diametroInterior(self):
        return (self.diametroExterior()-(2*2.25*self.modulo))
    
e1 = Engranaje(20,2,0)
print(f"El diámetro exterior es: {e1.diametroExterior()}")
print(f"El diámetro primitivo es: {e1.diametroPrimitivo()}")
print(f"El diámetro interior es: {e1.diametroInterior()}")