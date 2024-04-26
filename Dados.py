import random

def tirar_dado():
    dado = random.randint(1, 6)
    return dado

def juego():
    puntosJuan = estrategia_juan()
    puntosMaria = estrategia_maria(puntosJuan)
    print("      RESULTADO    \n----------------------\n| Nombre |  Puntos   |\n----------------------\n| Juan   |    ", puntosJuan, "    |\n| María  |    ", puntosMaria, "    |\n----------------------")
    if puntosJuan > puntosMaria:
        print("GANADOR: JUAN")
    elif puntosMaria > puntosJuan:
        print("GANADOR: MARÍA")
    else:
        print("EMPATE")

def estrategia_juan():
    puntosJuan = 0
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    print("\nPRIMER LANZAMIENTO JUAN\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
    if dado1 == 4 or dado2 == 4:
        puntosJuan = dado1 + dado2 - 4
        print("Puntuación: ", puntosJuan, "\n")
        if dado1 < 4:
            print("Lanza de nuevo el dado 1")
            dado1 = tirar_dado()
        if dado2 < 4:
            print("Lanza de nuevo el dado 2")
            dado2 = tirar_dado()
        if dado1 == 4 or dado2 == 4:
            puntosJuan = dado1 + dado2 - 4
    else:
        print("Puntuación", puntosJuan, "\n")
        print("Lanza de nuevo ambos dados")
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        print("\nSEGUNDO LANZAMIENTO JUAN\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
        if dado1 == 4 or dado2 == 4:
            puntosJuan = dado1 + dado2 - 4
        else: 
            puntosJuan = 0
    print("Puntuación Final de Juan: ", puntosJuan, "\n")
    return puntosJuan
        
def estrategia_maria(puntosJuan):
    puntosMaria = 0
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    print("\nPRIMER LANZAMIENTO MARÍA\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
    if dado1 == 4 or dado2 == 4:
        puntosMaria = dado1 + dado2 - 4
        print("Puntuación:", puntosMaria, "\n")
        if puntosMaria > puntosJuan:
            print ("María se retira\n")
            return puntosMaria
        else:
            if dado1 == 4 & dado2 == 4:
                print("Lanza de nuevo uno de los dados")
                dado2 = tirar_dado()
            elif dado1 < 4:
                print("Lanza de nuevo el dado 1")
                dado1 = tirar_dado()
            elif dado2 < 4:
                print("Lanza de nuevo el dado 2")
                dado2 = tirar_dado()
            if dado1 == 4 or dado2 == 4:
                puntosMaria = dado1 + dado2 - 4
    else:
        print("Puntuación: ", puntosMaria, "\n")
        print("Lanza de nuevo ambos dados")
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        print("\nSEGUNDO LANZAMIENTO MARÍA\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
        if dado1 == 4 or dado2 == 4:
            puntosMaria = dado1 + dado2 - 4
        else: 
            puntosMaria = 0
    print("Puntuación Final de María: ", puntosMaria, "\n")
    return puntosMaria

juego()