def es_palindromo(texto):

    texto = texto.lower()
    texto = ''.join(letra for letra in texto if letra.isalnum())

    #Verificar si el texto es igual al texto al reves
    return texto == texto[::-1]

def main():
    entrada = input("Escribe una palabra o frase: ")
    if es_palindromo(entrada):
        print(f'"{entrada}" es un palindromo.')
    else:
        print(f'"{entrada}" no es un palindromo.')

if __name__ == "__main__":
    main()