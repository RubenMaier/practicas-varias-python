"""
r read (leer)
w write (escribir)
a append (agregar al final)
r+ read and write (leer y escribir)

para evitar usar open para abrir el archivo y close para cerrarlo, 
podemos usar keywords como with (es un manejador de contexto que nos evita perder memoria)

with open('file', 'r') as archivo:
    for linea in archivo:
        print(linea)

sin with debemos hacerlo asi:

try:
    archivo = open('file', 'r')
    for linea in archivo:
        print(linea)
finally:
    archivo.close()

archivo.write("algo") me permite escribir en el archivo
archivo.readLines() me lee cada linea, y una linea se considera desde el comienzo hasta el primer \n

"""