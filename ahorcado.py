# -*- coding: utf-8 -*-
import random

""" 
    El juego comienza con una horca vacia y una palabra dividias en letras
    Vamos ingresando letras por consola y nos va añadiendo partes del cuerpo del ahorcado
    si es que no acertamos, caso contrario se autocompletará la letra ingresada.
    Si la persona ahorcada se completa, perdimos.
    Las palabras son randoms de un cojunto definido.
"""

IMAGENES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

PALABRAS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def palabra_random():
    indice = random.randint(0, len(PALABRAS) - 1) # nos retorna un elemento random de la lista
    return PALABRAS[indice]

def actualizar_imagen(palabra_escondida, intentos_fallidos):
    # mostramos de la lista imagen, el indice correspondiente a la cantidad de intentos fallidos que tenga
    print(IMAGENES[intentos_fallidos])
    print('')
    print(palabra_escondida)
    print("Intentos fallidos: ", intentos_fallidos, "/ 7")
    print("---------------------------------------------------------------------------------")

def chequearExistencia(palabra, letra_ingresada):
    letras_correcta = []
    for idx in range(len(palabra)): # itero a lo largo de nuestra palabra
        # si alguno de los caracteres de la palabra es igual al ingresado
        if palabra[idx] == letra_ingresada:
            # añado la letra ingresada en la lista de correctas exactamente en el indice que ocupa en la palabra
            letras_correcta.append(idx)
    return letras_correcta

def notificarGameOver(palabra, palabra_escondida, intentos_fallidos):
    actualizar_imagen(palabra_escondida, intentos_fallidos)
    print('')
    print('!PERDISTE! La palabra correcta era', palabra)

def notificarVictoria(palabra):
    print('')
    print('¡GANASTE! La palabra correcta era', palabra)

def jugar():
    palabra = palabra_random()
    palabra_escondida = ['-'] * len(palabra)
    intentos_fallidos = 0
    while True:
        actualizar_imagen(palabra_escondida, intentos_fallidos)
        letra_ingresada = ''
        while len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            letra_ingresada = input('Escoge una letra valida [A...z]: ').lower()
        letras_correcta = chequearExistencia(palabra, letra_ingresada)
        if len(letras_correcta) == 0:
            # si no atinamos con ninguna letra, aumentamos los intentos fallidos
            intentos_fallidos += 1
            if intentos_fallidos == 7:
                notificarGameOver(palabra, palabra_escondida, intentos_fallidos)
                break
        else:
            # si letras_correctas no es vacio, significa que tengo alguna
            for idx in letras_correcta:
                # itero a travez de todas las letras correctas que tenga y añado en palabras_escondidas la letra correcta en su correspondiente lugar/indice
                palabra_escondida[idx] = letra_ingresada
            # formateo letras_correctas para la proxima iteración
            letras_correcta = []
            # si no quedan elementos de tipo "-" significa que ya encontramos todas las letras
            if str(palabra_escondida).find('-') == -1:
                notificarVictoria(palabra)
                break

if __name__ == '__main__':
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")
    print("------------------------Bienvenidos al juego del ahorcado------------------------")
    print("---------------------------------------------------------------------------------")
    jugar()