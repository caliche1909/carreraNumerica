import os
import time
import random


def request_number_of_players():
    while True:
        try:           
            num_jugadores = int(input("Ingresa el numero de jugadores (2-4): "))
            if 2 <= num_jugadores <= 4:
                return num_jugadores
            else:
                os.system('clear')
                print("Error: Debes ingresar un número entre 2 y 4.")
        except ValueError:
            os.system('clear')
            print("Error: Por favor, ingresa un número válido.")

def request_level():
    while True:
        try:
            print("*****Seleccione el nivel de la partida*****")
            print("")
            print("1. Nivel basico ( Tablero de 20 posiciones )")
            print("2. Nivel intermedio ( Tablero de 30 posiciones )")
            print("3. Nivel avanzado ( Tablero de 50 posiciones )")
            print("4. Nivel experto (Tablero de 100 pocisiones)")
            level = int(input(""))  

            if 1 <= level <= 4:
                return level
            else:
                os.system('clear')
                print("Seleccione una opcion valida")
        except ValueError:
            os.system('clear')
            print("Error: Por favor, ingresa un número válido.")

def addLevel(level):
    if level == 1:
        numPuestos = 20
        print("***NIVEL BASICO***")
    elif level  == 2:
        numPuestos = 30
        print("***NIVEL INTERMEDIO***")
    elif level == 3:
        numPuestos = 50
        print("***NIVEL AVANZADO***")
    elif level == 4:
        numPuestos = 100
        print("***NIVEL EXPERTO***")
       
    print(f"Preparando tablero para recorrer {numPuestos} casillas....") 
    time.sleep(2)    
    os.system('clear')

    return numPuestos 

def roll_dice ():
    total_dices = []
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total_dices.append(dice1)
    total_dices.append(dice2)
    return total_dices

def play_turn(player, positions, total_positions):
    print(f"Turno del jugador {player}")
    distance_to_finish = total_positions - positions[player]

    # Determinar si se necesitan lanzar uno o dos dados
    if distance_to_finish <= 6:
        dice_results = [random.randint(1, 6)]
    else:
        dice_results = roll_dice()

    dice_total = sum(dice_results)
    print(f"Dado 1: {dice_results[0]}")
    if len(dice_results) == 2:
        print(f"Dado 2: {dice_results[1]}")
    print(f"Total: {dice_total}")

    # Calcular nueva posición
    new_position = positions[player] + dice_total
    if new_position > total_positions:
        print("¡Ups! Te has pasado. No te mueves en este turno.")
        print("*************************************************************")
    else:
        positions[player] = new_position
        print(f"El jugador {player} avanza a la posición {positions[player]}")
        print("*************************************************************")

        if positions[player] == total_positions:
            time.sleep(2)
            os.system("clear")
            print(f"FELICIDADES ***JUGADOR {player}*** HAZ GANADO EL JUEGO")
            print("*************************************************************")
            time.sleep(5)
            return player
        else:
            return None
    

def is_game_over(positions, total_positions):
    return any(pos == total_positions for pos in positions)
