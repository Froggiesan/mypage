#imports
import os
import random
import readchar



#The games works better in terminal/cmd than tipical run in pycharm
#pokemons
pikachu = 100
charmanderLife = 60
bolbasolLife = 60
makigarkLife= 35
digelLife = 25

#constants
POS_X = 0
POS_Y = 1
npc_number = 4
turn = 0
Win_medal = []

#coordenate_Game_chacters
my_Position = [9, 11]
npc_charmander = [9, 3]
npc_bolbasol = [16 , 10]
npc_magikar = [2, 10]
npc_digel = [9, 18]


#map_Variables
obstacleMap = ["▓", "▒", "█", "╦", "╩", "»", "«"]
pokeMap = """\
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
▓▒▒▒▒▒▒▒    ▒▒▒▒▒▒▓
▓▒▒▒▒▒▒      ▒▒▒▒▒▓
▓▒▒▒▒▒        ▒▒▒▒▓
▓▒▒▒▒          ▒▒▒▓
▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▓
▓╦╦╦╦╦╦╦╦  ╦╦╦╦╦╦╦▓
▓»»»»»»»»  «««««««▓
▓       »  «      ▓
▓       »  «      ▓
▓       ░  ░      ▓
▓       »  «      ▓
▓»»»»»»»»  «««««««▓
▓╩╩╩╩╩╩╩╩  ╩╩╩╩╩╩╩▓
▓████████░░███████▓
▓████          ███▓
▓█████        ████▓
▓██████      █████▓
▓███████    ██████▓
▓█████████████████▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\
"""
pokeMap = [list(row) for row in pokeMap.split("\n")]
mapWidth = len(pokeMap[0])
mapHeight = len(pokeMap)
pokemon_ASCII = """\
                                  ,'|
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|\

"""
pikachu_ascii = """\
       ,___          .-;'
       `"-.`\_...._/`.`
    ,      \        /
 .-' ',    / ()   ()|
`'._   \  /()    .  (|
    > .' ;,     -'-  /
   / <   |;,     __.;
   '-.'-.|  , \    , |
      `>.|;, \_)    \_)
       `-;     ,    /
          \    /   <
           '. <`'-,_)
            '._)\
"""
print(pokemon_ASCII)
entrenador = input("¿ Como te llamas ?")
os.system("cls")
print(pikachu_ascii)
print("Bien {} , aqui tienes a tu pokemon".format(entrenador))
print("Para moverte por el mapa usa WASD || Para salir del juego solo pulsa Q")
input("¡Presiona ENTER para seguir!")
#while of npc and character positions.
while npc_number != 0:
    os.system("cls")
    print("╔" + "=" * mapWidth * 2 + "╗")
    for coor_Y in range(mapHeight):
        print("║", end="")
        for coor_X in range(mapWidth):
            char_to_draw = "  "
            npc_in_cell = None
            # Creating the pokemon symbols
            if npc_charmander[POS_X] == coor_X and npc_charmander[POS_Y] == coor_Y and 1 not in Win_medal:
                char_to_draw = " ☼"
                npc_in_cell = npc_charmander

            elif npc_charmander[POS_X] == coor_X and npc_charmander[POS_Y] == coor_Y and 1 in Win_medal:
                char_to_draw = " x"

            if npc_bolbasol[POS_X] == coor_X and npc_bolbasol[POS_Y] == coor_Y and 2 not in Win_medal:
                char_to_draw = " !"
                npc_in_cell = npc_bolbasol

            elif npc_bolbasol[POS_X] == coor_X and npc_bolbasol[POS_Y] == coor_Y and 2 in Win_medal:
                char_to_draw = " x"

            if npc_digel[POS_X] == coor_X and npc_digel[POS_Y] == coor_Y and 3 not in Win_medal:
                char_to_draw = " @"
                npc_in_cell = npc_digel

            elif npc_digel[POS_X] == coor_X and npc_digel[POS_Y] == coor_Y and 3 in Win_medal:
                char_to_draw = " x"

            if npc_magikar[POS_X] == coor_X and npc_magikar[POS_Y] == coor_Y and 4 not in Win_medal:
                char_to_draw = " %"
                npc_in_cell = npc_magikar

            elif npc_magikar[POS_X] == coor_X and npc_magikar[POS_Y] == coor_Y and 4 in Win_medal:
                char_to_draw = " x"

            if my_Position[POS_X] == coor_X and my_Position[POS_Y] == coor_Y:
                char_to_draw = " ☻"

                if npc_in_cell == npc_charmander:
            #pokemon combat
                    while pikachu > 0 and bolbasolLife > 0:
                        print("\n+++++++++++++++++++++++++++++++++++")
                        turn += 1
                        print("Enfrentamiento contra campeón Pokemon tipo fuego.")
                        print("Turno {}: Pikachu".format(turn))
                        print("+++++++++++++++++++++++++++++++++++")
                        pikachu_Attack = 0
                        charmander_Attack = 0
                        op = 0

                        while op not in [1, 2, 3, 4]:
                            op = int(input("Elige el ataque de Pikachu: "
                                           "\n1. Ataque rapido."                        
                                           "\n2. Curación."
                                           "\n3. Corte."
                                           "\n4. Impactrueno"
                                           "\nElige tu ataque: "))
                            if op > 4:
                                print("Elige una opcion valida.")
                        error = random.randint(1, 4)
                        if op == 1:
                            pikachu_Attack = 15
                            print("-----------------------------------------")
                            print("Pikachu usa Ataque rapido...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("Pikachu intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("Pikachu no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                pikachu += 20
                                if pikachu >= 100:
                                    pikachu = 100
                                pikachu_bar = int(pikachu / 10)
                                print("-----------------------------------------")
                                print("Pikachu se ha curado, ahora su vida es \n[{}]({}/100)\n".format(pikachu_bar * "#",
                                                                                                       pikachu))
                                print("-----------------------------------------")
                        if op == 3:
                            pikachu_Attack = 12
                            print("-----------------------------------------")
                            print("Pikachu usa corte...")
                            print("-----------------------------------------")
                        if op == 4:
                            pikachu_Attack = 7
                            print("-----------------------------------------")
                            print("Pikachu usa impact trueno...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. charmander esta ileso.")
                        else:
                            charmanderLife -= pikachu_Attack
                            if charmanderLife <= 0:
                                charmanderLife = 0
                                print("Vida actual de Pikachu \n[]({}/100)\n".format(charmanderLife))
                                print("¡¡¡Pikachu ha ganado el duelo!!!\n¡¡¡Obtienes la medalla de agua!!!"
                                      "\n Presiona cualquier tecla de movimiento para mostrar "
                                      "correctamente el mapa.")
                                turn = 0
                                pikachu = 100
                                Win_medal.append(1)
                                npc_number -= 1
                                break
                            else:
                                charmander_Bar = int(charmanderLife / 10)
                                print("Vida actual de charmander\n[{}]({}/100)\n".format(charmander_Bar * "#",
                                                                                        charmanderLife))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                        print("***********************************")
                        print("Turno {}: Charmander".format(turn))
                        print("***********************************")
                        op = random.randint(1, 4)
                        error = random.randint(1, 4)
                        if op == 1:
                            charmander_Attack = 13
                            print("-----------------------------------------")
                            print("Charmander usa Placaje...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("Charmander intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("Charmander no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                charmanderLife += 20
                                if charmanderLife >= 100:
                                    charmanderLife = 100
                                charmander_Bar = int(charmanderLife / 10)
                                print("-----------------------------------------")
                                print("Charmander se ha curado, ahora su vida es: \n[{}]({}/100)\n".format(
                                    charmander_Bar * "#",
                                    charmanderLife))
                                print("-----------------------------------------")
                        if op == 3:
                            charmander_Attack = 10
                            print("-----------------------------------------")
                            print("Charmander usa Lanzallamas...")
                            print("-----------------------------------------")
                        if op == 4:
                            charmander_Attack = 9
                            print("-----------------------------------------")
                            print("Charmander usa Latigo...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. Pikachu esta ileso.")
                        else:
                            pikachu -= charmander_Attack
                            if pikachu <= 0:
                                pikachu = 0
                                print("Vida actual de Pikachu\n[]({}/100)\n".format(pikachu))
                                print("Charmander ha ganado el duelo. Intenta de nuevo derrotar a este maestro Pokemon\n"
                                      "Presiona cualquier tecla de movimiento para intentar nuevamente.")
                                turn = 0
                                pikachu = 100
                                charmanderLife = 100
                                break
                            else:
                                pikachu_bar = int(pikachu / 10)
                                print("Vida actual de Pikachu \n[{}]({}/100)\n".format(pikachu_bar * "#", pikachu))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                elif npc_in_cell == npc_bolbasol:
                    while pikachu > 0 and bolbasolLife > 0:
                        print("\n+++++++++++++++++++++++++++++++++++")
                        turn += 1
                        print("Enfrentamiento contra campeón Pokemon tipo hierba.")
                        print("Turno {}: Pikachu".format(turn))
                        print("+++++++++++++++++++++++++++++++++++")
                        pikachu_Attack = 0
                        bolbasol_Attack = 0
                        op = 0
                        while op not in [1, 2, 3, 4]:
                            op = int(input("Elige el ataque de Pikachu: "
                                           "\n1. Ataque rapido."                     
                                           "\n2. Curación."
                                           "\n3. corte"
                                           "\n4. Impactrueno"
                                           "\nElige tu ataque: "))
                            if op > 4:
                                print("Elige una opcion valida.")
                        error = random.randint(1, 4)
                        if op == 1:
                            pikachu_Attack = 15
                            print("-----------------------------------------")
                            print("Pikachu ha usado ataque rapido...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("Pikachu intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("Pikachu no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                pikachu += 20
                                if pikachu >= 100:
                                    pikachu = 100
                                pikachu_bar = int(pikachu / 10)
                                print("-----------------------------------------")
                                print("Pikachu se ha curado, ahora su vida es \n[{}]({}/100)\n".format(pikachu_bar * "#",
                                                                                                       pikachu))
                                print("-----------------------------------------")
                        if op == 3:
                            pikachu_Attack = 12
                            print("-----------------------------------------")
                            print("Pikachu ha usado corte...")
                            print("-----------------------------------------")
                        if op == 4:
                            pikachu_Attack = 7
                            print("-----------------------------------------")
                            print("Pikachu ha usado impact treno...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. bulbasaur esta ileso.")
                        else:
                            bolbasolLife -= pikachu_Attack
                            if bolbasolLife <= 0:
                                bolbasolLife = 0
                                print("Vida actual de bolbasol\n[]({}/100)\n".format(bolbasolLife))
                                print("¡¡¡Pikachu ha ganado el duelo!!!\n¡¡¡Obtienes la medalla de hierba!!!"
                                      "\n Presiona cualquier tecla de movimiento para mostrar "
                                      "correctamente el mapa.\n")
                                turn = 0
                                pikachu = 100
                                Win_medal.append(2)
                                npc_number -= 1
                                break
                            else:
                                charizardBar = int(bolbasolLife / 10)
                                print("Vida actual de bolbasol\n[{}]({}/100)\n".format(charizardBar * "#",
                                                                                        bolbasolLife))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                        print("***********************************")
                        print("Turno {}: bolbasol".format(turn))
                        print("***********************************")
                        op = random.randint(1, 4)
                        error = random.randint(1, 4)
                        if op == 1:
                            bolbasol_Attack = 16
                            print("-----------------------------------------")
                            print("bolbasol usa Arañazo...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("bolbasol intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("bolbasol no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                bolbasolLife += 20
                                if bolbasolLife >= 100:
                                    bolbasolLife = 100
                                charizardBar = int(bolbasolLife / 10)
                                print("-----------------------------------------")
                                print("bolbasol se ha curado, ahora su vida es \n[{}]({}/100)\n".format(
                                    charizardBar * "#",
                                    bolbasolLife))
                                print("-----------------------------------------")
                        if op == 3:
                            bolbasol_Attack = 13
                            print("-----------------------------------------")
                            print("bolbasol usa Gruñido...")
                            print("-----------------------------------------")
                        if op == 4:
                            bolbasol_Attack = 10
                            print("-----------------------------------------")
                            print("bolbasol usa fotosintesis...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. Pikachu esta ileso.")
                        else:
                            pikachu -= bolbasol_Attack

                            if pikachu <= 0:
                                pikachu = 0
                                print("Vida actual de Pikachu\n[]({}/100)\n".format(pikachu))
                                print("Bolbasol ha ganado el duelo. Intenta de nuevo derrotar a este maestro Pokemon\n"
                                      "Presiona cualquier tecla de movimiento para intentar nuevamente.")
                                turn = 0
                                pikachu = 100
                                bolbasolLife = 100
                                break
                            else:
                                pikachu_bar = int(pikachu / 10)
                                print("Vida actual de Pikachu\n[{}]({}/100)\n".format(pikachu_bar * "#", pikachu))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                elif npc_in_cell == npc_digel:
                    while pikachu > 0 and digelLife > 0:
                        print("\n+++++++++++++++++++++++++++++++++++")
                        turn += 1
                        print("Enfrentamiento contra campeón Pokemon tipo tierra.")
                        print("Turno {}: Pikachu".format(turn))
                        print("+++++++++++++++++++++++++++++++++++")
                        pikachu_Attack = 0
                        digel_Attack = 0
                        op = 0
                        while op not in [1, 2, 3, 4]:
                            op = int(input("Elige el ataque de Pikachu: "
                                           "\n1. Ataque rapido."
                                           "\n2. Curación."
                                           "\n3. corte."
                                           "\n4. Impact Trueno"
                                           "\nElige tu ataque: "))
                            if op > 4:
                                print("Elige una opcion valida.")
                        error = random.randint(1, 4)
                        if op == 1:
                            pikachu_Attack = 15
                            print("-----------------------------------------")
                            print("Pikachu ha usado ataque rapido...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("Pikachu intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("Pikachu no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                pikachu += 20
                                if pikachu >= 100:
                                    pikachu = 100
                                pikachu_bar = int(pikachu / 10)
                                print("-----------------------------------------")
                                print("Pikachu se ha curado, ahora su vida es \n[{}]({}/100)\n".format(pikachu_bar * "#",
                                                                                                       pikachu))
                                print("-----------------------------------------")
                        if op == 3:
                            pikachu_Attack = 12
                            print("-----------------------------------------")
                            print("Pikachu ha utilizado corte...")
                            print("-----------------------------------------")
                        if op == 4:
                            pikachu_Attack = 7
                            print("-----------------------------------------")
                            print("Pikachu ha usado impact trueno...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. digel esta ileso.")
                        else:
                            digelLife -= pikachu_Attack
                            if digelLife <= 0:
                                digelLife = 0
                                print("Vida actual de Digel\n[]({}/100)\n".format(digelLife))
                                print("¡¡¡Pikachu ha ganado el duelo!!!\n¡¡¡Obtienes la medalla de tipo tierra!!!"
                                      "\n Presiona cualquier tecla de movimiento para mostrar "
                                      "correctamente el mapa.")
                                turn = 0
                                pikachu = 100
                                Win_medal.append(3)
                                npc_number -= 1
                                break
                            else:
                                digel_Bar = int(digelLife / 10)
                                print("Vida actual de digel\n[{}]({}/100)\n".format(digel_Bar * "#",
                                                                                        digelLife))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                        print("***********************************")
                        print("Turno {}: digel".format(turn))
                        print("***********************************")
                        op = random.randint(1, 4)
                        error = random.randint(1, 4)
                        if op == 1:
                            digel_Attack = 13
                            print("-----------------------------------------")
                            print("digel usa Arañazo...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("digel  intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("digel no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                digelLife += 20
                                if digelLife >= 100:
                                    digelLife = 100
                                digel_Bar = int(digelLife / 10)
                                print("-----------------------------------------")
                                print("digel se ha curado, ahora su vida es \n[{}]({}/100)\n".format(
                                    digel_Bar * "#",
                                    digelLife))
                                print("-----------------------------------------")
                        if op == 3:
                            digel_Attack = 10
                            print("-----------------------------------------")
                            print("digel usa terremeto...")
                            print("-----------------------------------------")
                        if op == 4:
                            digel_Attack = 10
                            print("-----------------------------------------")
                            print("digel usa Guardia Baja...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. Pikachu esta ileso.")
                        else:
                            pikachu -= digel_Attack

                            if pikachu <= 0:
                                pikachu = 0
                                print("Vida actual de Pikachu\n[]({}/100)\n".format(pikachu))
                                print("digel ha ganado el duelo. Intenta de nuevo derrotar a este maestro Pokemon\n"
                                      "Presiona cualquier tecla de movimiento para intentar nuevamente.")
                                turn = 0
                                pikachu = 100
                                digelLife = 100
                                break
                            else:
                                pikachu_bar = int(pikachu / 10)
                                print("Vida actual de Pikachu\n[{}]({}/100)\n".format(pikachu_bar * "#", pikachu))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                elif npc_in_cell == npc_magikar:
                    while pikachu > 0 and makigarkLife > 0:
                        print("\n+++++++++++++++++++++++++++++++++++")
                        turn += 1
                        print("Enfrentamiento contra campeón Pokemon tipo agua.")
                        print("Turno {}: Pikachu".format(turn))
                        print("+++++++++++++++++++++++++++++++++++")
                        pikachu_Attack = 0
                        magikar_Attack = 0
                        op = 0
                        while op not in [1, 2, 3, 4]:
                            op = int(input("Elige el ataque de Pikachu: "
                                           "\n1. Ataque rapido"
                                           "\n2. Curación."
                                           "\n3. Corte."
                                           "\n4. Lazer umbral"
                                           "\nElige tu ataque: "))
                            if op > 4:
                                print("Elige una opcion valida.")
                            elif op != [1,2,3,4]:
                                op = random.randint(1, 4)
                                print("Tu pokemon no te ha entendido! Utilizará...")
                        error = random.randint(1, 4)
                        if op == 1:
                            pikachu_Attack = 15
                            print("-----------------------------------------")
                            print("Pikachu ha usado ataque rapido...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("Pikachu intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("Pikachu no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                pikachu += 20
                                if pikachu >= 100:
                                    pikachu = 100
                                pikachu_bar = int(pikachu / 10)
                                print("-----------------------------------------")
                                print("Pikachu se ha curado, ahora su vida es \n[{}]({}/100)\n".format(pikachu_bar * "#",
                                                                                                       pikachu))
                                print("-----------------------------------------")
                        if op == 3:
                            pikachu_Attack = 12
                            print("-----------------------------------------")
                            print("Pikachu ha usado corte...")
                            print("-----------------------------------------")
                        if op == 4:
                            pikachu_Attack = 7
                            print("-----------------------------------------")
                            print("Pikachu ha usado impact trueno...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El Pikachu ha fallado. magikar esta ileso.")
                        else:
                            makigarkLife -= pikachu_Attack
                            if makigarkLife <= 0:
                                makigarkLife = 0
                                print("Vida actual de magikar\n[]({}/100)\n".format(digelLife))
                                print("¡¡¡Pikachu ha ganado el duelo!!!\n¡¡¡Obtienes la medalla de tipo agua!!!"
                                      "\n Presiona cualquier tecla de movimiento para mostrar "
                                      "correctamente el mapa.")
                                turn = 0
                                pikachu = 100
                                Win_medal.append(4)
                                npc_number -= 1
                                break
                            else:
                                machampBar = int(makigarkLife / 10)
                                print("Vida actual de magikar\n[{}]({}/100)\n".format(machampBar * "#", makigarkLife))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
                        print("***********************************")
                        print("Turno {}: magikar".format(turn))
                        print("***********************************")
                        op = random.randint(1, 4)
                        error = random.randint(1, 4)
                        if op == 1:
                            magikar_Attack = 15
                            print("-----------------------------------------")
                            print("magikar usa Salpicar...")
                            print("-----------------------------------------")
                        if op == 2:
                            print("-----------------------------------------")
                            print("magikar intenta curarse...")
                            print("-----------------------------------------")
                            if error == 3:
                                print("-----------------------------------------")
                                print("magikar no ha podido curarse.")
                                print("-----------------------------------------")
                            else:
                                makigarkLife += 20
                                if makigarkLife >= 100:
                                    makigarkLife = 100
                                machampBar = int(makigarkLife / 10)
                                print("-----------------------------------------")
                                print("magikar se ha curado, ahora su vida es \n[{}]({}/100)\n".format(machampBar * "#",
                                                                                                       makigarkLife))
                                print("-----------------------------------------")
                        if op == 3:
                            magikar_Attack = 13
                            print("-----------------------------------------")
                            print("magikar usa aquajet...")
                            print("-----------------------------------------")
                        if op == 4:
                            magikar_Attack = 10
                            print("-----------------------------------------")
                            print("magikar onda sonica...")
                            print("-----------------------------------------")
                        if error == 3 and op != 2:
                            print("El ataque ha fallado. Pikachu esta ileso.")
                        else:
                            pikachu -= magikar_Attack

                            if pikachu <= 0:
                                pikachu = 0
                                print("Vida actual de Pikachu\n[]({}/100)\n".format(pikachu))
                                print("magikar ha ganado el duelo. Intenta de nuevo derrotar a este maestro Pokemon\n"
                                      "Presiona cualquier tecla de movimiento para intentar nuevamente.")
                                turn = 0
                                pikachu = 100
                                makigarkLife = 100
                                break
                            else:
                                pikachu_bar = int(pikachu / 10)
                                print("Vida actual de Pikachu\n[{}]({}/100)\n".format(pikachu_bar * "#", pikachu))
                        input("\nPresiona enter para continuar... \n")
                        os.system("cls")
#if draw final map

            if pokeMap[coor_Y][coor_X] == "▓":
                char_to_draw = "▓▓"

            if pokeMap[coor_Y][coor_X] == "▒":
                char_to_draw = "▒▒"

            if pokeMap[coor_Y][coor_X] == "░":
                char_to_draw = "░░"

            if pokeMap[coor_Y][coor_X] == "█":
                char_to_draw = "██"

            if pokeMap[coor_Y][coor_X] == "╦":
                char_to_draw = "╦╦"

            if pokeMap[coor_Y][coor_X] == "╩":
                char_to_draw = "╩╩"

            if pokeMap[coor_Y][coor_X] == "»":
                char_to_draw = "»»"

            if pokeMap[coor_Y][coor_X] == "«":
                char_to_draw = "««"
            print("{}".format(char_to_draw), end="")
        print("║")
    print("╚" + "=" * mapWidth * 2 + "╝")

#movimiento del personaje.
    direction = readchar.readchar().decode()
    newPosition = None

    if direction == "w":
        newPosition = [my_Position[POS_X], (my_Position[POS_Y] - 1) % mapWidth]

    elif direction == "s":
        newPosition = [my_Position[POS_X], (my_Position[POS_Y] + 1) % mapWidth]

    elif direction == "d":
        newPosition = [(my_Position[POS_X] + 1) % mapWidth, my_Position[POS_Y]]

    elif direction == "a":
        newPosition = [(my_Position[POS_X] - 1) % mapWidth, my_Position[POS_Y]]

    elif direction == "q":
        os.system("cls")
        print("Saliendo del juego...")
        exit()

    if newPosition:
        if pokeMap[newPosition[POS_Y]][newPosition[POS_X]] not in obstacleMap:

            my_Position = newPosition
print("Eres le mejor entrenador pokemon!")
