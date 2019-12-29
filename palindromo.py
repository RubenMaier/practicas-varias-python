def esPalindromo(palabra):
    palabra_invertida = palabra[::-1]  # invierto la palabra
    return palabra == palabra_invertida


if __name__ == '__main__':  #  punto de entrada o arranque
    palabra = input('Escribe una palabra: ')
    resultado = esPalindromo(palabra)
    if resultado is True:
        print("La palabra ", palabra, "ingresada es palindromo")
    else:
        print("La palabra ", palabra, "ingresada NO es palindromo")
