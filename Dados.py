import random

def tirar_dado():
    dado = random.randint(1, 6)
    return dado

def juego():
    cantidadJuegosString = input("Ingrese cuantas veces quiere simular el juego, 1000, 10000 o 100000: ")
    cantidadJuegos = int(cantidadJuegosString)
    cantVictoriasJuan = 0
    cantVictoriasMaria = 0
    cantEmpates = 0
    while(cantidadJuegos>0):
        puntosJuan = estrategia_juan()
        puntosMaria = estrategia_maria(puntosJuan)
        print("      RESULTADO    \n----------------------\n| Nombre |  Puntos   |\n----------------------\n| Juan   |    ", puntosJuan, "    |\n| Maria  |    ", puntosMaria, "    |\n----------------------")
        if puntosJuan > puntosMaria:
            print("GANADOR: JUAN")
            cantVictoriasJuan+=1
        elif puntosMaria > puntosJuan:
            print("GANADOR: MARiA")
            cantVictoriasMaria+=1
        else:
            print("EMPATE")
            cantEmpates+=1
        cantidadJuegos = cantidadJuegos - 1
        
    print("Cantidad de victorias de Juan", cantVictoriasJuan)
    print("Cantidad de victorias de Maria", cantVictoriasMaria)
    print("Empates", cantEmpates)
    
             

def estrategia_juan():
    puntosJuan = 0
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    print("\nPRIMER LANZAMIENTO JUAN\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
    if dado1 == 4 or dado2 == 4:
        puntosJuan = dado1 + dado2 - 4
        print("Puntuacion: ", puntosJuan, "\n")
        if dado1 < 4:
            print("Lanza de nuevo el dado 1...")
            dado1 = tirar_dado()
        if dado2 < 4:
            print("Lanza de nuevo el dado 2...")
            dado2 = tirar_dado()
        if dado1 == 4 or dado2 == 4:
            puntosJuan = dado1 + dado2 - 4
    else:
        print("Puntuacion", puntosJuan, "\n")
        print("Juan lanza de nuevo ambos dados...")
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        if dado1 == 4 or dado2 == 4:
            puntosJuan = dado1 + dado2 - 4
        else: 
            puntosJuan = 0
    print("\nSEGUNDO LANZAMIENTO JUAN\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
    print("Puntuacion Final de Juan: ", puntosJuan, "\n")
    return puntosJuan
        
def estrategia_maria(puntosJuan):
    puntosMaria = 0
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    print("\nPRIMER LANZAMIENTO MARiA\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
    if dado1 == 4 or dado2 == 4:
        puntosMaria = dado1 + dado2 - 4
        print("Puntuacion:", puntosMaria, "\n")
        if puntosMaria > puntosJuan:
            print ("Maria se retira\n")
            return puntosMaria
        else:
            if dado1 == 4 & dado2 == 4:
                print("Lanza de nuevo uno de los dados...")
                dado2 = tirar_dado()
            elif dado1 < 4:
                print("Lanza de nuevo el dado 1...")
                dado1 = tirar_dado()
            elif dado2 < 4:
                print("Lanza de nuevo el dado 2...")
                dado2 = tirar_dado()
            if dado1 == 4 or dado2 == 4:
                puntosMaria = dado1 + dado2 - 4
    else:
        print("Puntuacion: ", puntosMaria, "\n")
        print("Maria lanza de nuevo ambos dados...")
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        if dado1 == 4 or dado2 == 4:
            puntosMaria = dado1 + dado2 - 4
        else: 
            puntosMaria = 0
    print("\nSEGUNDO LANZAMIENTO MARiA\n-----------------------\n|  DADO 1  |  DADO 2  |\n-----------------------\n|    ", dado1, "    |   ", dado2, "   |\n-----------------------")
    print("Puntuacion Final de Maria: ", puntosMaria, "\n")
    return puntosMaria


juego()
