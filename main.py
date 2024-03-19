import os
import time
from game_functions import request_number_of_players, request_level, addLevel, play_turn, is_game_over



def menu ():
    os.system('clear')
    print("*****Bienvenidos a la carrera numerica*****")
    print("")
    number_of_players = request_number_of_players()
    os.system('clear')
    print(f"Preparando el juego para {number_of_players} jugadores....")
    time.sleep(2)
    os.system('clear')
    level = request_level()
    os.system('clear')
    numPuestos = addLevel(level)

    positions = {i: 0 for i in range(1, number_of_players + 1)}

     # Iniciar juego
    current_player = 1
    game_over = False
    while not game_over:
        winner = play_turn(current_player, positions, numPuestos)
        if winner is not None:
            print(f"¡Felicidades! El jugador {winner} ha ganado.")
            game_over = True
        else:
            current_player = (current_player % number_of_players) + 1
        time.sleep(1)                    
    print("***************** GAME OVER **********************")

menu()