"""
La siguiente función nos encuentra el primer CARACTER que NO se repite dentro de una PALABRA
ejemplos:
- "abacabad" -> c
- "abacabaabacaba" -> (-1) ninguno
- "bcccccccccccccyb" -> y
"""

def primer_caracter_no_repetido(palabra):
    caracteres_vistos = {} # diccionario vacio
    for idx, caracter in enumerate(palabra): 
        # enumerate nos crea una tupla de pares ordenados de (indice, caracter) 
        # ej: si la palabra es "hola" será [(0,"h"),(1,"h"),(2,"o"),(3,"l"),(4,"a")]
        if caracter not in caracteres_vistos:
            caracteres_vistos[caracter] = (idx, 1)
        else:
            caracteres_vistos[caracter] = (caracteres_vistos[caracter][0], caracteres_vistos[caracter][1] + 1) # le dejo el idx asignado por primera vez, pero le sumo 1 al segundo parametro de la tupla
    # nos vamos a quedar solo con las tuplas que tienen valor 1 en el segundo parametro
    caracteres_finales = [] # lista vacia, que la llenaremos con aquellos caracteres que se repitieron 1 sola vez
    for clave, valor in caracteres_vistos.items(): # items devuelve un iterador sobre los pares (clave, valor) del diccionario
        if valor[1] == 1: # si el valor, que en este caso es la cantidad de veces que se repitio una letra antes es 1...
            caracteres_finales.append( (clave, valor[0]) ) # significa que se repitio 1 sola vez el caracter, asi que lo añado a mi lista
    # ordenamos la lista en funcion del valor (es decir, cantidad de veces que se repitio)
    caracteres_finales_no_repetidos_y_ordenados = sorted(caracteres_finales, key = lambda valor: valor[1])
    if caracteres_finales_no_repetidos_y_ordenados:
        return caracteres_finales_no_repetidos_y_ordenados[0][0] # primer elemento de la lista que es la tupla, y el primer elemento de esa tupla que es la letra
    else:
            return '_'

if __name__ == '__main__':
    palabra = input('Escribe una palabra o secuencia de caracteres: ')
    resultado = primer_caracter_no_repetido(palabra)
    if resultado == '_':
        print('Todos los caracteres se repiten')
    else:
        print('El primer caracter no repetido es: {}'.format(resultado))