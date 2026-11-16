
from tamagochi import Tamagochi 
from helpers import show_statistics, show_tamagochis
import random as rng
import json


def rng_number():
    return rng.randint(1, 4)

def save_game(tam_list):
    tam_stats = []
    for tam in tam_list:
        tam_stats.append(tam.return_statistics_as_list())

    with open("game_save.json", 'w') as file:
        json.dump(tam_stats, file)

def load_game():
    try:
        with open("game_save.json", 'r') as file:
            tam_list_json = json.load(file)
            new_tam_list = []
            for tam_json in tam_list_json:
                new_tam = Tamagochi(tam_json[0], int(tam_json[1]), int(tam_json[2]), int(tam_json[3]), int(tam_json[4]), bool(tam_json[5]))
                new_tam_list.append(new_tam)
            return new_tam_list
    except Exception as e:
        print(f"Could not load game: {e}")
        return []

def select_tamagochi(tam_list):
    show_tamagochis(tam_list)
    selected_tam = input()
    tam = next((x for x in tam_list if x.name == selected_tam), None)

    while tam is None:
        print("Tamagochi not found. Select one from the list")
        selected_tam = input()
        tam = next((x for x in tam_list if x.name == selected_tam), None)

    return tam

def read_hours():
    print("For how many hours?")
    try:
        hours = int(input())
        if hours < 0:
            raise ValueError
        return hours
    except ValueError:
        print("Invalid number of hours")
        return None


def main():
    print ("Press a Key to play | Q - To Quit | Load - Load Game")
    command = input()
    tam_list = []
    while (command != "Q"):
        if command == "Load":
            tam_list = load_game()
            if len(tam_list) == 0:
                print ("Press a Key to play | Q - To Quit | Load - Load Game")
                command = input()
                continue
        else:
            a = Tamagochi(name="Tammy")
            tam_list.append(a)
            b = Tamagochi(name="Cesar")
            tam_list.append(b)
            c = Tamagochi(name="Luna")
            tam_list.append(c)
        
        tam = select_tamagochi(tam_list)

        print(f"---------- You have chosen {tam.name} ----------")

        print("F - Feed | S - Sleep | P - Play |" \
            " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
            " Save - Save Game | Load - Load | Q - Quit")
        command = input()

        while command != "Q":
            if tam.is_alive():
                if command == "F":
                    hours = read_hours()
                    if hours is not None:
                        tam.feed(hours)
                        num = rng_number()
                        tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()

                elif command == "S":
                    hours = read_hours()
                    if hours is not None:
                        tam.sleep(hours)
                        num = rng_number()
                        tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
    
                elif command == "P":
                    hours = read_hours()
                    if hours is not None:
                        tam.play(hours)
                        num = rng_number()
                        tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " Save - Save Game | Load - Load | Q - Quit")
                    command = input()
    
                elif command == "H":
                    hours = read_hours()
                    if hours is not None:
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

                elif command == "Load":
                    new_tam_list = load_game()
                    if len(new_tam_list) > 0:
                        tam_list = new_tam_list
                        tam = select_tamagochi(tam_list)
                        print(f"---------- You have chosen {tam.name} ----------")

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

            elif command == "Load":
                new_tam_list = load_game()
                if len(new_tam_list) > 0:
                    tam_list = new_tam_list
                    tam = select_tamagochi(tam_list)
                    print(f"---------- You have chosen {tam.name} ----------")

                print("F - Feed | S - Sleep | P - Play |" \
                    " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                    " Save - Save Game | Load - Load | Q - Quit")
                command = input()

            else:
                print(f"This tamagochi is dead. Please let it rest in peace")
                tam = select_tamagochi(tam_list)
                
                print("F - Feed | S - Sleep | P - Play |" \
                    " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                    " Save - Save Game | Load - Load | Q - Quit")
                command = input()
