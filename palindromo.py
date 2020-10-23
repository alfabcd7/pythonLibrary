def palindromo(palabra):
    palabra = palabra.replace(' ','') #Reemplaza todos los caracteres "Espaciados" por "vacio"
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False



def run():
     print("Averigua si es un palindromo")
     palabra = input("Ingresa una frase.: ")
     es_palindromo = palindromo(palabra)
     if es_palindromo == True:
         print("Es un palindromo")
     else:
        print("No es un palindromo")


if __name__ == '__main__':
    run()
