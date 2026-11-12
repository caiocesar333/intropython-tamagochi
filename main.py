
from tamagochi import Tamagochi 
import random as rng

tam_list = []

def rng_number():
    return rng.randint(1, 3)

def show_tamagochis():
    for tam in tam_list:
        print("---------- List of Tamagochis ----------")
        tam.show_name()
        print("Select one of the above (write the name)")

def main():

    a = Tamagochi(name="Caio")
    tam_list.append(a)

    print ("Press a Key to play | Q - To Quit")
    command = input()
    while (command != "Q"):
        
        show_tamagochis()

        selected_tam = input()

        tam = next(x for x in tam_list if x.show_name() == selected_tam)
        print("F - Feed | S - Sleep | P - Play |" \
            " H - Heal | Status - Show Status |" \
            " S - Save Game | L - Load | Q - Quit")
        command = input()
        while command != "Q":
            if command == "F":
                print("For how many hours?")
                hours = int(input())
                tam.feed(hours)
                num = rng_number()
                tam.random_event(num)
                print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status |" \
                                " S - Save Game | L - Load | Q - Quit")
                command = input()
            elif command == "S":
                print("For how many hours?")
                hours = int(input())
                tam.sleep(hours)
                num = rng_number()
                tam.random_event(num)
                print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status |" \
                                " S - Save Game | L - Load | Q - Quit")
                command = input()

            elif command == "P":
                print("For how many hours?")
                hours = int(input())
                tam.play(hours)
                num = rng_number()
                tam.random_event(num)
                print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status |" \
                                " S - Save Game | L - Load | Q - Quit")
                command = input()

            elif command == "H":
                print("For how many hours?")
                hours = int(input())
                tam.heal(hours)
                num = rng_number()
                tam.random_event(num)
                print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status |" \
                                " S - Save Game | L - Load | Q - Quit")
                command = input()

            elif command == "Status":
                tam.show_status()
                print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status |" \
                                " S - Save Game | L - Load | Q - Quit")
                command = input()

            else:
                print("Wrong command")
                print("F - Feed | S - Sleep | P - Play |" \
                                " H - Heal | Status - Show Status |" \
                                " S - Save Game | L - Load | Q - Quit")
                command = input()
                print(command)



