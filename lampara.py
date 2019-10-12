# -*- coding: utf-8 -*-

class LamparaDeEscritorio:
    # variable de clase
    # en python todo en mayusculas significa que la variable es una constante
    _LAMPARAS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    # el siguiente metodo es el contructur, que ejecutamos cuando instanaciamos un nuevo elemento de la clase
    # en python, algo que empiece con "__" significa que si lo toco se rompe, asi que mejor no tocar
    def __init__(self): # self es la propia clase (los metodos de clase reciben el parametro class)
        self._esta_encendida = False # variable privada

    def encender(self): # metodo publico
        self._esta_encendida = True
        self._actualizar_imagen()

    def apagar(self): # metodo publico
        self._esta_encendida = False
        self._actualizar_imagen()

    # si algo empieza con "_" significa que es privado, sea una funcion o una variable
    def _actualizar_imagen(self): # metodo privado
        if self._esta_encendida:
            print(self._LAMPARAS[0])
        else:
            print(self._LAMPARAS[1])

def ejecutar():
    lampara = LamparaDeEscritorio()

    while True:
        comando = input('''
            ¿Qué deseas hacer?
            [p]render
            [a]pagar
            [s]alir
        ''')
        if comando == 'p':
            lampara.encender()
        elif comando == 'a':
            lampara.apagar()
        else:
            break


if __name__ == '__main__':
    ejecutar()