#Before anything I need to load in my required libraries 
import random #This library will be used for a lot of the game functionalities
import time #For delaying text
import sys #For the text effect

#####
"""
1. First I need to define a name variable and make sure only letters are allowed in the name variable. 
2. Then I need to print a greeting to the user using their name.
3. I want to make it so the "Enter a valid name" only shows up if the user enters an invalid name.
4. This is coming back from a future section after I've created the delayed text output, but I need to create flashing text for "prompts"
"""
#####

def type_text(text, delay=0, emphasis=0, pause=0):
    """This will take a regular f-string and make the letters come out 1 by 1
    
    **text**: Just any character variables

    **delay**: Determines how long to wait before typing out the letters (Set to *0.05*)
    
    **emphasis**: Mainly for ellipsis (Set to *1*)

    **pause**: Mainly for commas (Set to *0.1*)
    """
    for letter in text: #This is taking the concept of what we did in chapter 7, if you give a char type as a "range" then the char is treated as a list etc. 
        sys.stdout.write(letter) #These two lines do the magic. "stdout" is just standard output and write will type out the letters without printing a new line like how python does defaultly
        sys.stdout.flush() #This makes it so python doesn't wait until the end to output everything

        if letter == ".": #Conditionals to slow down text when met with certain symbols
            time.sleep(emphasis)
        elif letter == ",": #I doubt the order matters in this case
            time.sleep(pause)
        else:
            time.sleep(delay)

    print()


type_text("\033[1;35mWhat is your name? >>>\033[m")
name = input() #Initializing the variable so the while loop knows what "name" is.

while not name.isalpha(): #isalpha makes sure user input is only letters.
    type_text("\033[1;35mPlease enter a valid name with only letters.\033[m\n")
    type_text("\033[1;35mWhat is your name? >>>\033[m")
    name = input()


#####
"""
1. I need to create the intro/tutorial text
2. I don't want the text to come out all at once, but one by one in like in many other games I've played (This might be done second but will appear first in code lines)
3. Find a way to make name text unique (This was done with ANSI)
"""
#####


### Start Village Chief Dialogue (Some prologue and initiation into the tutorial)
type_text(f"\n\033[36mVillage Chief:\033[0m Hello, \033[35m{name}\033[m! Welcome to Bherna Village!") #I changed the text color with the inbuilt ANSI formatting!

type_text(f"\033[36mVillage Chief:\033[0m You must be the hunter that the Guild sent over ...")

type_text(f"\033[36mVillage Chief:\033[0m It's not that I doubt your strength, but you don't really look like a hunter.")

type_text(f"\033[36mVillage Chief:\033[0m Before we have you hunt the real problem, why don't you show us what you've got by hunting that \033[32mKulu-Ya-Ku\033[m that's been stealing all our eggs?\n")


#####
"""
1. Need to create a yes/no option for the user to select or type in.
"""
#####
type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
Decision_Kulu = input()

# while not Decision_Kulu.isalpha(): #isalpha makes sure user input is only letters.
#     type_text("\033[1;35mPlease enter a valid answer with only letters.\033[m\n")
#     type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
#     Decision_Kulu = input()

while Decision_Kulu != "y" and Decision_Kulu != "n": #These conditions make checking if the input is a char redundant
    type_text("\033[1;35mPlease enter a valid answer from the options provided [y/n].\033[m\n")
    type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
    Decision_Kulu = input()

#####
"""
1. I need to start creating the game options and figure out randomizer
2. First the monster will have at least 5 attacks that come out at a "random" discrete chance
3. After trying to get health I realized there needs to be some interaction between health and dmg
"""
#####

#making lists of the monster attack names and their dmg values or ranges (I think I'll have to move all of this to the top)
Kulu_Attacks = [("Screech", (1, 2)), 
                ("Peck", (2, 3)),
                ("Hip Check", (5, 5)),
                ("Egg Throw", (4, 6)),
                ("Rock Throw", (4, 10))]

Rathalos_Attacks = [("Roar", (2, 3)),
                    ("Rush", (5, 6)),
                    ("Tail Sweep", (6, 8)),
                    ("Fly", (8, 9)),
                    ("Fire Ball", (10, 15))]

Bloobath_Calm = [("Wail", (5, 6)),
                 ("Horn Attack", (10, 12)),
                 ("Tail Sweep", (12, 13)),
                 ("Dig", (15, 20)),
                 ("Rush", (20, 25))]

Bloodbath_Enraged = [("Wail", (10, 12)),
                     ("Overheat", (20, 25)),
                     ("Tail Smash", (20, 23)),
                     ("Dig", (22, 28)),
                     ("Raging Rush", (25, 30))]


#The seperator lines just help me see the different sections better.
def combat(name, monster_name): 
    """This is the main combat loop"""

    #Defining the Health of the player and monsters
    player_HP = 30

    if monster_name == "Kulu-Ya-Ku":
        monster_HP = 25
    elif monster_name == "Rathalos":
        monster_HP = 50
    elif monster_name == "Bloodbath Diablos":
        monster_HP = 100
#----------------------------------------------------------------------------------------------------------------

    #Monster Introduction text
    type_text(f"\n\033[32mA wild {monster_name} appears!\033[m")

#----------------------------------------------------------------------------------------------------------------
    #This is the main loop 
    while player_HP > 0 and monster_HP > 0:
        type_text(f"\033[35m{name}\033[m HP: {player_HP}  |  \033[32m{monster_name}\033[m HP: {monster_HP}")

        #The player's turn 
        type_text(f"\033[1;35m[a] Attack \n[b] Block \n[h] Heal\033[m")
        player_choice = input().lower().strip()

        while player_choice not in ("a", "b", "h"):
            type_text("\033[1;35mPlease enter a valid answer from the options provided [a/b/h].\033[m\n")
            type_text(f"\033[1;35m[a] Attack \n[b] Block \n[h] Heal\033[m")
            player_choice = input().lower().strip()
        
        defense = 0

#----------------------------------------------------------------------------------------------------------------
        #Still in the player loop but making the if statements for each choice
        if player_choice == "a":
            player_roll = random.randint(1, 20) #Roll the dice!

            if player_roll <= 5:
                dmg = 0
            elif player_roll > 5 and player_roll < 18:
                dmg = 5
            elif player_roll >= 18:
                dmg = 10

            monster_HP -= dmg

            if player_roll <= 5:
                type_text(f"You swing wildly! ... but it misses.")
            elif player_roll > 5 and player_roll < 18:
                type_text(f"You swing true and deal \033[31m{dmg}\033[m damage!")
            elif player_roll >= 18:
                type_text(f"You swing by pure instinct! You deal \033[31m{dmg}\033[m damage!")
            
        elif player_choice == "b":
            player_roll = random.randint(1, 20) #Roll the dice!

            if player_roll <= 5:
                defense = 0
            elif player_roll > 5 and player_roll < 18:
                defense = 2
            elif player_roll >= 18:
                defense = 5

            if player_roll <= 5:
                type_text(f"You hold your Greatsword awkwardly to block and drop it ...")
            elif player_roll > 5 and player_roll < 18:
                type_text(f"You make your grip firm and brace to block \033[31m{defense}\033[m damage!")
            elif player_roll >= 18:
                type_text(f"Your guard is on point! You block \033[31m{defense}\033[m damage!")
        
        elif player_choice == "h":
            heal_amt = 10
            player_HP += heal_amt
            type_text(f"You drink a potion and recover \033[32m{heal_amt}\033[m HP.")
#----------------------------------------------------------------------------------------------------------------
        #Monster's turn
        if monster_name == "Kulu-Ya-Ku":
            monster_atk = random.choice(Kulu_Attacks)
        elif monster_name == "Rathalos":
            monster_atk = random.choice(Rathalos_Attacks)
        elif monster_name == "Bloodbath Diablos":
            if monster_HP > 50:
                monster_atk = random.choice(Bloobath_Calm)
            else:
                monster_atk = random.choice(Bloodbath_Enraged)

        monster_dmg = random.randint(monster_atk[1][0], monster_atk[1][1])
        monster_dmg = max(0, monster_dmg - defense)

        player_HP -= monster_dmg
        type_text(f"\n\033[32m{monster_name}:\033[m {monster_atk[0]}! It deals \033[31m{monster_dmg}\033[m damage!")

#----------------------------------------------------------------------------------------------------------------
    #Out of the while loop now and just checking who won
    if player_HP <= 0:
        type_text(f"\033[1;31mYou have been defeated...\033[m")
        return False
    else:
        type_text(f"\033[1;32mYou defeated {monster_name}!\033[m")
        return True

#####
"""
1. I moved the decision down here so I can actually use the combat() function
2. I need to confirm that answering "n" will end the game and not just skip the combat, and that "y" will start the combat
"""
#####

result = None
if Decision_Kulu == "y": #I don't think there's any need for this to have a final else statment since the conditions above should cover it
    type_text(f"\n\033[36mVillage Chief:\033[m Great! I'll lead you to it right now!")
    result = combat(name, "Kulu-Ya-Ku")

elif Decision_Kulu == "n":
    type_text(f"\n\033[36mVillage Chief:\033[m Too scared? We don't need someone like you around, go back to wherever you came from!")
    sys.exit()


#----------------------------------------------------------------------------------------------------------------
###Kulu-Ya-Ku defeated, now Rathalos decision and combat

#Text depending on if you won or lost
if result == True:
    type_text(f"\n\033[36mVillage Chief:\033[m Impressive! You really are a hunter! Then I trust you to handle our bigger problem ...")
    type_text(f"\033[36mVillage Chief:\033[m The King of the Skies ... that damned \033[31mRathalos\033[m! It's been burning our crops and destroying nearby villages. Will you take care of it?")
else:
    type_text(f"\n\033[36mVillage Chief:\033[m What a shame ... I really wanted to believe in you, but you're no hunter. Go back to wherever you came from!")
    sys.exit()

#Decision if won
type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
Decision_Rathalos = input()

#Ensures decision is valid
while Decision_Rathalos != "y" and Decision_Rathalos != "n": #These conditions make checking if the input is a char redundant
    type_text("\033[1;35mPlease enter a valid answer from the options provided [y/n].\033[m\n")
    type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
    Decision_Rathalos = input()

#Choices based on decision
result = None
if Decision_Rathalos == "y":
    type_text(f"\n\033[36mVillage Chief:\033[m I knew you had it in you! I'll lead you to it right now!")
    result = combat(name, "Rathalos")
elif Decision_Rathalos == "n":
    type_text(f"\n\033[36mVillage Chief:\033[m ... you're no hunter, go back to wherever you came from!")
    sys.exit()












