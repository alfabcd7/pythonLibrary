#The idea is develop an Script who make by itself a potentition of two since 0 to 1000.


def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()
