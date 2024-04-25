import random

def tirar_dado():
    dado = random.randint(1, 6)
    return dado

def juego():
    puntosJuan = estrategia_juan()
    puntosMaria = estrategia_maria(puntosJuan)
    if puntosJuan > puntosMaria:
        print("Gana Juan")
    elif puntosMaria > puntosJuan:
        print("Gana María")
    else:
        print("Empate")

def estrategia_juan():
    puntosJuan = 0
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    print("Dado 1: ", dado1,"\nDado 2: ", dado2)
    if dado1 == 4 or dado2 == 4:
        puntosJuan = dado1 + dado2 - 4
        print("Puntuación de Juan en el Primer Lanzamiento: ", puntosJuan)
        if dado1 < 4:
            print("Lanza de nuevo el dado 1")
            dado1 = tirar_dado()
        if dado2 < 4:
            print("Lanza de nuevo el dado 2")
            dado2 = tirar_dado()
        if dado1 == 4 or dado2 == 4:
            puntosJuan = dado1 + dado2 - 4
    else:
        print("Puntuación de Juan en el Primer Lanzamiento: ", puntosJuan)
        print("Lanza de nuevo ambos dados")
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        print("Dado 1: ", dado1,"\nDado 2: ", dado2)
        if dado1 == 4 or dado2 == 4:
            puntosJuan = dado1 + dado2 - 4
        else: 
            puntosJuan = 0
    print("Puntuación Final de Juan: ", puntosJuan)
    return puntosJuan
        
def estrategia_maria(puntosJuan):
    #!MODIFICAR ESTA FUNCIÓN DEPENDIENDO DE LA ESTRATEGIA DE MARÍA
    puntosMaria = 0
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    print("Dado 1: ", dado1,"\nDado 2: ", dado2)
    if dado1 == 4 or dado2 == 4:
        puntosMaria = dado1 + dado2 - 4
        print("Puntuación de María en el Primer Lanzamiento: ", puntosMaria)
        if dado1 < 4:
            print("Lanza de nuevo el dado 1")
            dado1 = tirar_dado()
        if dado2 < 4:
            print("Lanza de nuevo el dado 2")
            dado2 = tirar_dado()
        if dado1 == 4 or dado2 == 4:
            puntosMaria = dado1 + dado2 - 4
    else:
        print("Puntuación de María en el Primer Lanzamiento: ", puntosMaria)
        print("Lanza de nuevo ambos dados")
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        print("Dado 1: ", dado1,"\nDado 2: ", dado2)
        if dado1 == 4 or dado2 == 4:
            puntosMaria = dado1 + dado2 - 4
        else: 
            puntosMaria = 0
    print("Puntuación Final de Juan: ", puntosMaria)
    return puntosMaria

juego()