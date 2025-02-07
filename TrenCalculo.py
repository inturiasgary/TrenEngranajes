import pandas as pd
import pathlib
from math import sin, radians

Lista = '/Lista1.xlsx'
ruta = (str(pathlib.Path(__file__).parent.absolute()))+Lista
lista = pd.read_excel(ruta)

# Cargado de engranajes
df = pd.DataFrame(lista)
# paso = float(input("Ingrese valor inicial:"))
paso = 0.5
# paso = 20.6265*sin(radians(23))/13
# Conversión de excel a lista
Z = df['Z'].tolist()
cant = df['cantidad'].tolist()
r = []
f = 0
for z in Z:
    f += 1
    for x in Z:
        f += 1
        for y in Z:
            r.append((z, x, ((paso/z)*x)*y, y))
            f += 1

Resultado4 = []
Resultado5 = []
# # Filtrado para que sean engranajes existentes
for y in r:
    if (int(round(y[2])) in Z):
        Resultado4.append(y)
Resultado4.sort(key=lambda x: (abs(round(x[2])-x[2])), reverse=True)
for i in Resultado4:
    if (i[2]-int(i[2]) <= 1):
        print(i)

for i in Resultado4:
    Resultado5.append((i[0], i[1], int(round(i[2])), i[3]))

Resultado6 = []


for e in Resultado5:
    j = 0
    agregar = True
    for z in Z:
        if e.count(z) > cant[j]:
            agregar = False
            print(z, e.count(z), cant[j])
        j += 1
    if agregar == True:
        Resultado6.append(e)


print(Resultado6)
print(f'Calculos realizados: {f}')
