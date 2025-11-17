import json, os, sys
import requests
from colorama import Fore, Style
import random,time



def escape_dice(throw):
    throw = random.randint(1, 20) #It randomizes the number between 1 and 20
    print(throw)
    return throw

class Reptilian:
    def __init__(self, species, age):
        self.species = species
        self.age = int(age)


class Snake(Reptilian):
    def __init__(self, name, age, variant, species = 'Snake'):
        super().__init__(species, age)
        self.name = name
        self.variant = variant


class Frog(Reptilian):
    def __init__(self, name, age, variant, species = "Frog"):
        super().__init__(species, age)
        self.name = name
        self.variant = variant


def clear_key_buffer():
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

#First enemy
froggy_One = Frog("Fragger", 20, "Toad")
print(f"Name: {froggy_One.name} \nVariant: {froggy_One.variant}"
      f"\nSpecies: {froggy_One.species} Age: {froggy_One.age}")





req = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(req)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(f"The {froggy_One.name} tells you a random Chuck Norris joke:")
        print(json.dumps(data["value"], indent=2))
        print("It taunts you!")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa. Virhe =", e)


game_on = True
while game_on:
    print("----------------------------------------")
    print(Fore.CYAN + "         THE GAME BEGINS" + Style.RESET_ALL)

    frog_name = str(input("Enter your frog's name"))
    frog_age = int(input("Enter your frog's age"))
    frog_variant = str(input("Enter your frog's variant"))

    Player = Frog(frog_name,frog_age,frog_variant)
    if TypeError:
        print("INVALID TYPE")

    if Player:
        print("Success")
        print("Your adventure begins")
        clear_key_buffer()
    else:
        print("Your adventure ends here")
        print("Report the error")
    enemy = froggy_One
    print(f"Your enemy is {enemy.name}")
    print("What a shock")
    time.sleep(0.2)
    print("He starts chasing you. \nRUNNNN!!!!!!")
    print("Enter a number to throw the dice")
    print("If all goes well you'll escape")
    time.sleep(1)
    print("If not, sucks for you \nright?")
    dice = int(input("Enter an integer(example 5)"))


    result = escape_dice(dice)
    print(f"You threw {result}. WOW!")





