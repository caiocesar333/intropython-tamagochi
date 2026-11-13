
from tamagochi import Tamagochi 
from helpers import show_statistics, show_tamagochis
import random as rng

tam_list = []
a = Tamagochi(name="Caio")
tam_list.append(a)
b = Tamagochi(name="Cesar")
tam_list.append(b)

def rng_number():
    return rng.randint(1, 3)

def main():
    print ("Press a Key to play | Q - To Quit")
    command = input()
    while (command != "Q"):
        show_tamagochis(tam_list)
        selected_tam = input()
        tam = next((x for x in tam_list if x.show_name()
                    == selected_tam), tam_list[0])

        print(f"---------- You have chosen {tam.show_name()} ----------")

        print("F - Feed | S - Sleep | P - Play |" \
            " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
            " S - Save Game | L - Load | Q - Quit")
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
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
                elif command == "S":
                    print("For how many hours?")
                    hours = int(input())
                    tam.sleep(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
    
                elif command == "P":
                    print("For how many hours?")
                    hours = int(input())
                    tam.play(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
    
                elif command == "H":
                    print("For how many hours?")
                    hours = int(input())
                    tam.heal(hours)
                    num = rng_number()
                    tam.random_event(num)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
    
                elif command == "Status":
                    tam.show_status()
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
                    command = input()
    
                elif command == "Stat":
                    show_statistics(tam_list)
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
    
                else:
                    print("Wrong command")
                    
                    print("F - Feed | S - Sleep | P - Play |" \
                        " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                        " S - Save Game | L - Load | Q - Quit")
                    command = input()
            else:
                print(f"This tamagochi is dead. Please let it rest in peace")
                show_tamagochis(tam_list)
                selected_tam = input()
        
                tam = next(x for x in tam_list if x.show_name() == selected_tam)
                
                print("F - Feed | S - Sleep | P - Play |" \
                    " H - Heal | Status - Show Status | Stat - Show Game Statistics |" \
                    " S - Save Game | L - Load | Q - Quit")
                command = input()
        