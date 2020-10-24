def es_primo(numero):
    contador = 0


    for i in range(1,numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador = contador + 1
            print(str(contador))
    if contador == 0:
        return True
    else :
        return False 

def run():
    numero = int(input("Ingresa Un Numero para descubrir si es primo: "))
    if es_primo(numero):
        print("El numero q ingreso " + str(numero)  +" Es primo")
    else:
        print("El numero q ingreso " + str(numero)  +" NO es primo")    
    

if __name__ == "__main__":
    run()