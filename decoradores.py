# -*- coding: utf-8 -*-


password_constante = '123'


def password_requisitos(funcion_a_ejecutar):
    def wrapper():  # envoltura
        password_ingresada = input('¿Cual es tu contraseña? ')
        if(password_ingresada == password_constante):
            funcion_a_ejecutar()
        else:
            print('La contraseña no es correcta')
    return wrapper


@password_requisitos
def necesito_password():
    print('La contraseña es correcta')


def upper(funcion_a_ejecutar):
    # se utiliza este formato si la funcion a ejecutar trae argumentos propios necesarios para su correcta ejecución
    def wrapper(*args, **kwargs):
        resultado = funcion_a_ejecutar(*args, **kwargs)
        # las funciones a ejecutar y los resultados de un wrapper siempre deben retornar algo
        print(resultado.upper())
    return wrapper


@upper
def di_mi_nombre(nombre):
    return 'Hola, {}'.format(nombre)


if __name__ == '__main__':
    necesito_password()
    di_mi_nombre('Ruben')
