import os
import time
from Haunted_Mansion_Story import show_story
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_map():
    print("_________________________________")
    print('''
[Attic]
   |
  west
   |
[Stairs] -- east --> [Closet]
   |
  south
   |
[Basement] -- east --> [Kitchen] -- north --> [Hall]
''')
    print("__________________________________")

def showinstructions():
    print(
        '''
RPG GAME
__________
Commands:|_____
go [direction]|
get [item] |
show [map]|
------------    
        '''
    )

def status():
    print("________________________")
    print(f"Current room: {currentRoom}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        room_item = rooms[currentRoom]["item"]
        print(f"You see a {room_item}!")
    print("________________________")

inventory = []
currentRoom = "basement"

rooms = {
    "hall" : {
        "south" : "kitchen" ,
        "item" : "key" #Items in hall
             },
    "kitchen" : {
        "west" : "basement",
        "north" : "hall",
        "item" : "katana" #Items in kitchen
                },
    "basement" : {
          "north" : "stairs",
          "east" : "kitchen", #Items in the basement
                 },
    "stairs" : {
          "south" : "basement", #Stairs direction
          "east" : "closet",
          "west" : "attic",
          "item" : "cursed artifact"
               },
    "attic" : {
            "west" : "stairs",
            "item" : "monster" #Items in the attic
    },
    "closet" : {
         "west" : "stairs",
         "item" : "mysterious letter"
               }
}
directions = rooms[currentRoom]

game = True
#Shows the story
show_story()
#Waits 2 seconds
time.sleep(2)
#Shows instructions
showinstructions()
#Game start countdown
print("Game starts in")
for t in range(3, -1, -1):
    print(f"{t}s")
    time.sleep(1)

#Game loop begins
while game:

    status()

    move = input('>').strip().lower().split(" ", 1)
    #get sword -> [get, sword]

    #If the length of the list move is less than 2 items, does this
    if len(move) < 2:
        print("Invalid command, try go [direction] or get [item]")
        continue

    item_name = move[1]  # Second word is the item -> get [item]

    if move[0] == "get":
        if move[1] == rooms[currentRoom]["item"]:
            print(f"You got a {item_name}")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = ""
        else:
            print(f"You don't see a {item_name} here")
    #Move -> [go, north]
    if move[0] == "go":
        direction = move[1]
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][direction]
            print(f"You're now in the {currentRoom}!")
        else:
            print(f"You can't go {direction}")

    if move[0] == "show":
        if move[1] == "map":
            show_map()


    if "mysterious letter" in inventory:
        y_n = input("Do you want to read the letter? (yes/no)").lower().strip()
        if y_n == "yes":
            print("This mansion has been haunted for as long as I remember. "
                  "I can't keep living like this, I will end it soon!"
                  "\nIf you come here, don't go in the attic unprepared."
                  "There's a katana hidden somewhere in this house."
                  "\n1666 John Roberts")
            continue
        elif y_n == "no":
            continue
        else:
            print("WTF DUDE!")

    #Victory condition 1
    if "key" in inventory and "cursed artifact" in inventory:
        print("You escaped from the house of horrors!")
        print("You took the cursed artifact with you."
              "\nBefore unlocking the door you hear something from the attic"
              "\nGIVE THE CROSS BACK!!"
              "\nOh no, that didn't sound too good"
              "\nBE AWARE!")
        time.sleep(4)
        break

    #Loss condition and victory condition 2
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"].lower() == "monster":
        if "katana" in inventory:
            print("You reveal your blade and the monster shrieks")
            print("Fling! The blade cut the monsters head off")
            print("You defeated the monster, \nTHE HOUSE IS FREE, YOU WIN!")
            time.sleep(4)
            break
        else:
            print("You have been ripped in half by the monster")
            print("You died! Better luck next time")
            time.sleep(3)
            break


