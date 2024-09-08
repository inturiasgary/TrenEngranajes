Zc = float(input("Ingrese cantidad de dientes de herramienta:"))
Z = float(input("Ingrese cantidad de dientes de engranaje:"))
paso1 = ((5/3)*(Zc/Z))
ZT = [20, 24, 25, 30, 34, 36, 38, 40, 41, 42, 43, 44, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 54, 56, 58,
     60, 60, 62, 63, 64, 66, 68, 70, 72, 72, 74, 75, 76, 77, 78, 80, 81, 90, 91, 100, 102, 108, 120]
ZA = [20, 24, 25, 30, 34, 36, 38, 40, 41, 42, 43, 44, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 54, 56, 58,
     60, 60, 62, 63, 64, 66, 68, 70, 72, 72, 74, 75, 76, 77, 78, 80, 81, 90, 91, 100, 102, 108, 120]
ZB = [20, 24, 25, 30, 34, 36, 38, 40, 41, 42, 43, 44, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 54, 56, 58,
     60, 60, 62, 63, 64, 66, 68, 70, 72, 72, 74, 75, 76, 77, 78, 80, 81, 90, 91, 100, 102, 108, 120]
Resultado1 = []
Resultado2 = []
Resultado3 = []
for b in ZB:
    resultado1 = paso1/b
    Resultado1.append((b,resultado1))
for r in Resultado1:
    for a in ZA:
        Resultado2.append((r[0], a, r[1]*a))
for r in Resultado2:
    for a in ZA:
        Resultado3.append((r[0], r[1], a, r[2]*a))
sorted(Resultado3, key=lambda resultadoFinal: resultadoFinal[3])
Resultado4 = []
for y in Resultado3:
    if (int(y[3]) in ZT):
        Resultado4.append(y)
for i in Resultado4:
    if (i[3]-int(i[3])<=0.001):
        print(i)
