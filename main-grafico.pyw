from tkinter import *
from tkinter import messagebox
import os
import random

#Variables
codigoSecreto = []
contadorIntetos = 0
reglas = """PICAS Y FIJAS es un juego divertido que ayuda a aumentar tu nivel de lógica ,concentración y análisis.
El juego consiste en adivinar un NÚMERO SECRETO de 4 dígitos, el cual es generado aleatoriamente por el programa y permanece oculto. 
El programa suministra ayudas para adivinarlo llamadas PICAS o FIJAS.
Se obtiene una FIJA si acierta un dígito y su posición dentro del número secreto.
Se obtiene una PICA si acierta un dígito pero NO acierta su posición dentro del número secreto.
Se gana al adivinar el número secreto.
En el transcurso del juego se van mostrando los intentos y el tiempo recorrido.
Ejemplo: El programa crea el número secreto 9785, el jugador digíta 7381, el 8 es una FIJA ya que está en la posición correcta.
El 7 es una PICA ya que pertenece al número secreto pero no coincide en la posición.
A este juego también se le conoce como PUNTO y FAMA"""


#Mis funciones
def infoAyuda():
    messagebox.showinfo('Ayuda de Picas y Fijas', reglas)

def infoRealizado():
    messagebox.showinfo('Picas y Fijas realizado', 'Realizado por \n Carlos A Granada \n Julian A Granada')

def restart():
    raiz.destroy()
    os.startfile("main-grafico.pyw")

def crearBotonesReset():
    botonReiniciar = Button(miFrame, text="Intentalo", command=restart)
    botonReiniciar.grid(row=16,column=1)

def numeroUsurio():
    global contadorIntetos
    global codigoSecreto
    strinValidarNumero = ''
    try:
        validarNumero = int(numeroIngresadoUsuario.get())
        numeroIngresadoUsuario.set('')
        if (validarNumero < 999) or (validarNumero > 10000):
            labelError.config(text= 'Por favor el numero debe ser 4 digitos intenta de nuevo')
        else:
            contadorIntetos += 1
            contadorFiga = 0
            contarPica = 0
            strinValidarNumero = str(validarNumero)
            for r in range(4):
                if str(strinValidarNumero[r]) == str(codigoSecreto[r]):
                    contadorFiga += 1 
            for n in strinValidarNumero:
                for f in codigoSecreto:
                    if str(n) == str(f):
                        contarPica +=1
            lababelCF= Label(miFrame, text=f'Número de fijas: {contadorFiga} ')
            labelCP= Label(miFrame, text=f'Número de picas: {contarPica - contadorFiga}')
            lababelCF.grid(row=contadorIntetos,column=0, sticky='w')
            labelCP.grid(row=contadorIntetos,column=1, sticky='w')
            labelContador.config(text=f'Número de intento: {contadorIntetos}')
            labelContador.config(text=f'Número de intento: {contadorIntetos}')
            if (contadorFiga == 4) and (contadorIntetos < 4):
                labelMensaje.config(text= 'Bien, Excelente')
                cuadroTexto.destroy()
                botonPF.destroy()
                crearBotonesReset()
            elif (contadorFiga == 4) and (contadorIntetos < 8):
                labelMensaje.config(text= 'Bien, Aceptable')
                cuadroTexto.destroy()
                botonPF.destroy()
                crearBotonesReset()
            elif (contadorFiga == 4) and (contadorIntetos <= 12):
                labelMensaje.config(text= 'Bien, Regular')
                cuadroTexto.destroy()
                botonPF.destroy()
                crearBotonesReset()
            elif (contadorFiga != 4) and (contadorIntetos == 12):
                labelMensaje.config(text= 'Mal, este juego como que no es para ti')
                cuadroTexto.destroy()
                botonPF.destroy()
                crearBotonesReset() 
            labelError.config(text='')
    except ValueError:
        labelError.config(text= 'Por favor debe ser número de 4 digitos no texto')

for i in range(4):
    validacion = True 
    if (len(codigoSecreto) == 0):
        comienza = random.randint(1, 9)
        codigoSecreto.append(comienza)
    else:
        while validacion:
            val = False
            comienza = random.randint(0, 9)
            for g in codigoSecreto:
                if g == comienza:
                    val = True
            if val != True:
                val = False
                validacion = False
        codigoSecreto.append(comienza)

#iniciamos interface
raiz=Tk()
raiz.iconbitmap("icono.ico")
raiz.title('Picas y Fijas')

#Menu
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)
ayuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=ayuda)
ayuda.add_command(label="Como jugar", command=infoAyuda)
ayuda.add_command(label='Realizado por', command=infoRealizado)

#Cuerpo
intentos = 'Numero de intentos: 0'
numeroIngresadoUsuario = StringVar()
error = ""
mensaje = ""

miFrame=Frame(raiz,width=500, height=400)
miFrame.pack()

cuadroTexto= Entry(miFrame, textvariable=numeroIngresadoUsuario)
cuadroTexto.grid(row=13,column=0)

botonPF = Button(miFrame, text="Intentar", command=numeroUsurio)
botonPF.grid(row=13,column=1)

labelContador= Label(miFrame, text=intentos)
labelContador.grid(row=0, column=3, sticky='e')

labelError= Label(miFrame, text=error, fg='#FF0000')
labelError.grid(row=14, column=1, sticky='e')

labelMensaje= Label(miFrame, text=mensaje, fg='#0000ff')
labelMensaje.grid(row=15, column=1, sticky='e')


raiz.geometry("650x350")


# Ejecutador de la ventana
raiz.mainloop()