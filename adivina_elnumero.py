import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Ingresa un numero del 1 al 100: "))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print("ingresa un numero mas grande: ")
            
        else:
             print("ingresa un numero mas pequeño: ")   
        numero_elegido = int(input("Ingresa un numero: "))
    print("Ganaste")    



if __name__ == "__main__":
    run()