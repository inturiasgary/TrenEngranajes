from tkinter import ttk, PhotoImage, Label, Frame, Entry, Button, StringVar
import tkinter as tk
import re
from Engranaje import Engranaje


def validarFloat(string):
    regex = re.compile(r"(\+|\-)?[0-9.]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count('+') <= 1
                and string.count('-') <= 1
                and string.count(',') <= 1
                and result is not None
                and result.group(0) != ""))


def on_validarFloat(P):
    return validarFloat(P)


def validarInt(string):
    regex = re.compile(r"[0-9]*$")
    result = regex.match(string)
    return (string == ""
            or (result is not None
                and result.group(0) != ""))


def on_validarInt(P):
    return validarInt(P)


mainWindow = tk.Tk()
mainWindow.title("Aplicación cálculo Tren Engranajes")
icon = PhotoImage(file="icon.png")
mainWindow.iconphoto(True, icon)
mainWindow.geometry("400x650")
mainWindow.resizable(False, False)

tab = ttk.Notebook(mainWindow, height=600, width=350)
frameEngranaje = Frame(tab)
frameIzqEng = Frame(frameEngranaje, borderwidth=5)
frameDerEng = Frame(frameEngranaje, borderwidth=10)
frameAbaEng = Frame(frameEngranaje, borderwidth=5)
frameMaquina = Frame(tab)


tab.add(frameEngranaje, text="Engranaje")
tab.add(frameMaquina, text="Máquina")

tab.pack()


frameIzqEng.pack(side=tk.LEFT)
frameDerEng.pack(side=tk.RIGHT)
frameAbaEng.pack()

# Labels Engranaje

llistEngranaje = ["Cantidad de dientes:", "Módulo:",
                  "Ángulo:", "Diámetro Exterior:", "Diámetro Primitivo:", "Diámetro Interior:",
                  "Paso de hélice:", " "]

nrow = 0
for i in range(len(llistEngranaje)):
    Label(frameIzqEng, text=llistEngranaje[i], bd=5).grid(
        row=nrow, column=0, sticky=tk.E)
    nrow += 1

# Entrys Engranaje
eDientes = Entry(frameDerEng, text="Cantidad de dientes:",
                 bd=4, validate="key")
vcmd3 = (eDientes.register(on_validarInt), '%P')
eDientes.config(validatecommand=vcmd3)
eModulo = Entry(frameDerEng, text="Módulo:", bd=4, validate="key")
vcmd2 = (eModulo.register(on_validarFloat), '%P')
eModulo.config(validatecommand=vcmd2)
eAngulo = Entry(frameDerEng, text="Ángulo:", bd=4, validate="key")
vcmd = (eAngulo.register(on_validarFloat), '%P')
eAngulo.config(validatecommand=vcmd)
entradaDiametroExterior = StringVar()
eDiametroExt = Entry(frameDerEng, textvariable=entradaDiametroExterior,
                     bd=4, state="readonly")
entradaDiametroPrimitivo = StringVar()
eDiametroPri = Entry(
    frameDerEng, textvariable=entradaDiametroPrimitivo, bd=4, state="readonly")
entradaDiametroInterior = StringVar()
eDiametroInt = Entry(frameDerEng, textvariable=entradaDiametroInterior,
                     bd=4, state="readonly")
entradaPasoHelice = StringVar()
ePasoDeHelice = Entry(frameDerEng, textvariable=entradaPasoHelice,
                      bd=4, state="readonly")


def Calcular():
    engranaje = Engranaje(z=float(eDientes.get()), modulo=float(
        eModulo.get()), anguloHelice=float(eAngulo.get()))
    entradaDiametroExterior.set(str(round(engranaje.diametroExterior(), 3)))
    entradaDiametroPrimitivo.set(str(round(engranaje.diametroPrimitivo(), 3)))
    entradaDiametroInterior.set(str(round(engranaje.diametroInterior(), 3)))
    entradaPasoHelice.set(str(round(engranaje.pasoHelice(), 3)))


botonCalcular = Button(frameDerEng, text="Calcular", bd=4,
                       command=Calcular)

eDientes.pack()
eModulo.pack()
eAngulo.pack()
eDiametroExt.pack()
eDiametroPri.pack()
eDiametroInt.pack()
ePasoDeHelice.pack()
botonCalcular.pack()

lwm = Label(frameMaquina, text="Primer Label maquina", bd=4)
lwm.pack()


table = ttk.Treeview(frameMaquina, columns=(
    'A', 'B', 'C', 'D'), show='headings')
table.heading('A', text='A')
table.heading('B', text='B')
table.heading('C', text='C')
table.heading('D', text='D')
table.column("A", width=50, anchor='e')
table.column("B", width=50, anchor='e')
table.column("C", width=50, anchor='e')
table.column("D", width=50, anchor='e')

table.pack(fill='both', expand=True)

mainWindow.mainloop()
