from tkinter import *
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

def numeroUsurioCorrecto():
    numero = 0
    while (numero < 999) or (numero > 10000):
        while True:
            try:
                numero = int(input('Ingresa un número de 4 digitos:'))  
                break
            except ValueError:
                print('Por favor debe ser número de 4 digitos no texto')
        if numero < 999 or numero > 10000:
            print('Por favor el numero debe ser 4 digitos intenta de nuevo')
    return str(numero)
    

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

print(reglas)

for i in range(12):
    contadorIntetos += 1
    contadorFiga = 0
    contarPica = 0
    numeroUsuario = numeroUsurioCorrecto()
    for i in range(4):
        if str(numeroUsuario[i]) == str(codigoSecreto[i]):
            contadorFiga += 1 
    for i in numeroUsuario:
        for f in codigoSecreto:
            if str(i) == str(f):
                contarPica +=1
    print(f'Número de intento: {contadorIntetos} ')
    print(f'Número de fijas: {contadorFiga}')
    print(f'Número de picas: {contarPica - contadorFiga}')
    if contadorFiga == 4:
        break

if (contadorIntetos == 12) and (contadorFiga != 4):
    print('Mal, este juego como que no es para ti')


if (contadorIntetos >= 8) and (contadorFiga == 4):
    print('Bien, Regular')

if (contadorIntetos < 8) and (contadorIntetos >= 4) and (contadorFiga == 4):
    print('Bien, Aceptable')

if (contadorIntetos < 4) and (contadorFiga == 4):
    print('Bien, Excelente')