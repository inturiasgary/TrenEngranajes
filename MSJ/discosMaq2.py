import math
# VA = float(input("Ingrese valor inicial:"))
paso1 = 9.1036
# paso1 = 0.78141679
# ZA = [21,24,25,28,30,32,35,36,39,40,44,45,47,48,50,51,52,53,55,56]
# ZB = [58,60,64,66,70,71,72,73,74,75,76,79,80,84,86,88,90,96,100]
#Z = [21, 24, 25, 28, 30, 32, 35, 36, 39, 40, 44, 45, 47, 48, 50, 51, 52, 53, 55,
# 56, 58, 60, 64, 66, 70, 71, 72, 73, 74, 75, 76, 79, 80, 84, 86, 88, 90, 96, 100]
# ZA = [21, 24, 25, 28, 30, 32, 35, 36, 39, 40, 44, 45, 47, 48, 50, 51, 52, 53, 55,
#       56, 58, 60, 64, 66, 70, 71, 72, 73, 74, 75, 76, 79, 80, 84, 86, 88, 90, 96, 100]
# ZB = [21, 24, 25, 28, 30, 32, 35, 36, 39, 40, 44, 45, 47, 48, 50, 51, 52, 53, 55,
#       56, 58, 60, 64, 66, 70, 71, 72, 73, 74, 75, 76, 79, 80, 84, 86, 88, 90, 96, 100]
# ZT = [20, 21, 22, 24, 25, 28, 32, 36, 39, 40, 44, 45, 48,
#       51, 52, 56, 60, 64, 72, 74, 76, 81, 83, 86, 96, 100, 126]
Z = [20, 21, 22, 24, 25, 28, 32, 36, 39, 40, 44, 45, 48,
     51, 52, 56, 60, 64, 72, 74, 76, 81, 83, 86, 96, 100, 126]
# ZB = [20, 21, 22, 24, 25, 28, 32, 36, 39, 40, 44, 45, 48,
#       51, 52, 56, 60, 64, 72, 74, 76, 81, 83, 86, 96, 100, 126]
# Z = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#      36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]


Resultado1 = []
Resultado2 = []
Resultado3 = []
f = 0
# Primer FOR
for b in Z:
    resultado1 = paso1/b
    f += 1
    Resultado1.append((b, resultado1))
# print Resultado1
# Segundo FOR
for r in Resultado1:
    for a in Z:
        f += 1
        Resultado2.append((r[0], a, r[1]*a))
# print Resultado2

# Tercer FOR
for r in Resultado2:
    for a in Z:
        f += 1
        Resultado3.append((r[0], r[1], r[2]*a, a))
# Resultado3.sort()
# sorted(Resultado3, key=lambda resultadoFinal: resultadoFinal[3]) #estaba activo
Resultado4 = []
# # Filtrado para que sean engranajes existentes
for y in Resultado3:
    if (int(y[2]) in Z):
        Resultado4.append(y)
Resultado4.sort(key=lambda x: (float(x[2]-int(x[2]))), reverse=True)
for i in Resultado4:
    if (i[2]-int(i[2]) <= 0.1   ):
        print(i)
print(f'Calculos realizados: {f}')
