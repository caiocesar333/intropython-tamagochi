
from tamagochi import Tamagochi 
from helpers import show_statistics, show_tamagochis
import random as rng


def rng_number():
    return rng.randint(1, 3)

def save_game(tam_list):
    with open("game_save.txt", 'w') as file:
        for tam in tam_list:
            tam_stats = tam.return_statistics_as_list()
            file.write(f"{tam_stats}\n")

def load_game():
    try:
        with open("game_save.txt", 'r') as file:
            new_tam_list = []
            for line in file:
                json = line.replace(" ", "").replace('"', "").replace("]", "").replace("[", "").replace("\n", "").split(",")
                new_tam = Tamagochi(json[0], int(json[1]), int(json[2]), int( json[3]),int( json[4]), json[5] == "True")
                new_tam_list.append(new_tam)
            return new_tam_list
    except Exception as e:
        print(f"File not found: {e}")


def main():
    print ("Press a Key to play | Q - To Quit | Load - Load Game")
    command = input()
    tam_list = []
    while (command != "Q"):
        if command == "Load":
            tam_list = load_game()
            print(tam_list)
        else:
            a = Tamagochi(name="Caio")
            tam_list.append(a)
            b = Tamagochi(name="Cesar")
            tam_list.append(b)
        
        show_tamagochis(tam_list)
        selected_tam = input()
        tam = next((x for x in tam_list if x.show_name()
                    == selected_tam), tam_list[0])

        print(f"---------- You have chosen {tam.show_name()} ----------")

        print("F - Feed | S - Sleep | P - Play |" \
            " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
            " Save - Save Game | Load - Load | Q - Quit")
        command = input()

        while command != "Q":
            if tam.is_alive():
                if command == "F":
                    print("For how many hours?")
                    hours = int(input())
                    tam.feed(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()

                elif command == "S":
                    print("For how many hours?")
                    hours = int(input())
                    tam.sleep(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
    
                elif command == "P":
                    print("For how many hours?")
                    hours = int(input())
                    tam.play(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
    
                elif command == "H":
                    print("For how many hours?")
                    hours = int(input())
                    tam.heal(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
    
                elif command == "Status":
                    tam.show_status()
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
                    command = input()
    
                elif command == "Stat":
                    show_statistics(tam_list)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()

                elif command == "Save":
                            save_game(tam_list=tam_list)
                            
                            print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                                " Save - Save Game | Load - Load | Q - Quit")
                            command = input()

                else:
                    print("Wrong command")
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
                    
            elif command == "Save":
                save_game(tam_list=tam_list)
                
                print("F - Feed | S - Sleep | P - Play |" \
                    " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                    " Save - Save Game | Load - Load | Q - Quit")
                command = input()

            else:
                print(f"This tamagochi is dead. Please let it rest in peace")
                show_tamagochis(tam_list)
                selected_tam = input()
        
                tam = next((x for x in tam_list if x.show_name() == selected_tam),  tam_list[0])
                
                print("F - Feed | S - Sleep | P - Play |" \
                    " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                    " Save - Save Game | Load - Load | Q - Quit")
                command = input()
