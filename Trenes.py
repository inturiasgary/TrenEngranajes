import pandas as pd
import pathlib

Lista = '/Lista.xlsx'
ruta = (str(pathlib.Path(__file__).parent.absolute()))+Lista

print(ruta)
lista = pd.read_excel(ruta)
VA = float(input("Ingrese valor inicial:"))
paso1 = VA/240.0
# ZA = [21,24,25,28,30,32,35,36,39,40,44,45,47,48,50,51,52,53,55,56]
# ZB = [58,60,64,66,70,71,72,73,74,75,76,79,80,84,86,88,90,96,100]
# ZT = [21,24,25,28,30,32,35,36,39,40,44,45,47,48,50,51,52,53,55,56,58,60,64,66,70,71,72,73,74,75,76,79,80,84,86,88,90,96,100]
# ZA = [21,24,25,28,30,32,35,36,39,40,44,45,47,48,50,51,52,53,55,56,58,60,64,66,70,71,72,73,74,75,76,79,80,84,86,88,90,96,100]
# ZB = [21,24,25,28,30,32,35,36,39,40,44,45,47,48,50,51,52,53,55,56,58,60,64,66,70,71,72,73,74,75,76,79,80,84,86,88,90,96,100]
ZT = [20, 21, 22, 24, 25, 28, 32, 36, 39, 40, 44, 45,
      48, 51, 52, 56, 60, 64, 72, 74, 76, 86, 96, 100]
ZA = [20, 21, 22, 24, 25, 28, 32, 36, 39, 40, 44, 45,
      48, 51, 52, 56, 60, 64, 72, 74, 76, 86, 96, 100]
ZB = [20, 21, 22, 24, 25, 28, 32, 36, 39, 40, 44, 45,
      48, 51, 52, 56, 60, 64, 72, 74, 76, 86, 96, 100]
Resultado1 = []
Resultado2 = []
Resultado3 = []
for b in ZB:
    resultado1 = paso1/b
    Resultado1.append((b, resultado1))
# print Resultado1
for r in Resultado1:
    for a in ZA:
        Resultado2.append((r[0], a, r[1]*a))
# print Resultado2

for r in Resultado2:
    for a in ZA:
        Resultado3.append((r[0], r[1], a, r[2]*a))
# Resultado3.sort()
sorted(Resultado3, key=lambda resultadoFinal: resultadoFinal[3])
Resultado4 = []
# print Resultado4
for y in Resultado3:
    if (int(y[3]) in ZT):
        Resultado4.append(y)
for i in Resultado4:
    if (i[3]-int(i[3]) <= 0.03):
        print(i)

# Imprimiendo contenido de la lista
df = pd.DataFrame(lista)
print(df)
