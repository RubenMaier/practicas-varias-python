# -*- coding: utf-8 -*-


# la primer linea nos permite poder escribir caracteres de castellano latino en los mensajes

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def di_hola(self):
        print('Hola, so {} y tengo {} años'.format(self.nombre, self.edad))


if __name__ == '__main__':
    persona = Persona('Ruben', 25)
    print('Edad: {}'.format(persona.edad))
    persona.di_hola()
