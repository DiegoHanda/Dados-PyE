import random


def roll_dice():
    dice = random.randint(1, 6)
    return dice


def play_game():
    sim_games_string = input(
        "Ingrese cuantas veces quiere simular el juego: ")
    sim_games = int(sim_games_string)
    juan_wins = 0  # Cantidad de Victorias de Juan
    maria_wins = 0  # Cantidad de Victorias de María
    draws = 0  # Cantidad de Empates
    while (sim_games > 0):
        juan_score = juan_strategy()
        maria_score = maria_strategy(juan_score)
        if juan_score > maria_score:
            juan_wins += 1
        elif maria_score > juan_score:
            maria_wins += 1
        else:
            draws += 1
        sim_games = sim_games - 1
    print("\n      RESULTADO    \n  Ganador |  Total"
          "\n----------------------\n  Juan    |  ", juan_wins,
          "\n----------------------\n  Maria   |  ", maria_wins,
          "\n----------------------\n  Empate  |  ", draws, "\n")


def juan_strategy():
    juan_score = 0
    dice1 = roll_dice()
    dice2 = roll_dice()
    if dice1 == 4 or dice2 == 4:
        juan_score = dice1 + dice2 - 4
        if dice1 < 4:
            dice1 = roll_dice()
        if dice2 < 4:
            dice2 = roll_dice()
        if dice1 == 4 or dice2 == 4:
            juan_score = dice1 + dice2 - 4
    else:
        dice1 = roll_dice()
        dice2 = roll_dice()
        if dice1 == 4 or dice2 == 4:
            juan_score = dice1 + dice2 - 4
        else:
            juan_score = 0
    return juan_score


def maria_strategy(juan_score):
    maria_score = 0
    dice1 = roll_dice()
    dice2 = roll_dice()
    if dice1 == 4 or dice2 == 4:
        maria_score = dice1 + dice2 - 4
        if maria_score > juan_score:
            return maria_score
        else:
            if dice1 == 4 & dice2 == 4:
                dice2 = roll_dice()
            elif dice1 < 4:
                dice1 = roll_dice()
            elif dice2 < 4:
                dice2 = roll_dice()
            if dice1 == 4 or dice2 == 4:
                maria_score = dice1 + dice2 - 4
    else:
        dice1 = roll_dice()
        dice2 = roll_dice()
        if dice1 == 4 or dice2 == 4:
            maria_score = dice1 + dice2 - 4
        else:
            maria_score = 0
    return maria_score


play_game()
