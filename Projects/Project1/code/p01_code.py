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
    Decision_Kulu = input().strip().lower()

#####
"""
1. I need to start creating the game options and figure out randomizer
2. First the monster will have at least 5 attacks that come out at a "random" discrete chance
3. After trying to get health I realized there needs to be some interaction between health and dmg
"""
#####

#making lists (of tuples?) of the monster attack names and their dmg values or ranges (I think I'll have to move all of this to the top)
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


#Mass initializing variables I'll use to calculate dmg and stuff later
zenny = 0
attack_charm_amount = 0
defence_charm_amount = 0
healing_charm_amount = 0 
precision_charm_amount = 0
steadfast_charm_amount = 0
crit_charm_amount = 0
divine_blessing_amount = 0

charms = {
    "1": {"name": "Attack Charm", "cost": 10, "amount": attack_charm_amount},
    "2": {"name": "Defence Charm", "cost": 10, "amount": defence_charm_amount},
    "3": {"name": "Healing Charm", "cost": 10, "amount": healing_charm_amount},
    "4": {"name": "Precision Charm", "cost": 15, "amount": precision_charm_amount},
    "5": {"name": "Steadfast Charm", "cost": 15, "amount": steadfast_charm_amount},
    "6": {"name": "Crit Charm", "cost": 20, "amount": crit_charm_amount},
    "7": {"name": "Divine Blessing Charm", "cost": 25, "amount": divine_blessing_amount},
}

#The seperator lines just help me see the different sections better.
def combat(name, 
           monster_name, 
           zenny, 
           attack_charm_amount,
           defence_charm_amount,
           healing_charm_amount,
           precision_charm_amount,
           steadfast_charm_amount,
           crit_charm_amount,
           divine_blessing_amount): 
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

            if player_roll <= (5-precision_charm_amount):
                dmg = 0
            elif player_roll > (5-precision_charm_amount) and player_roll < (18-crit_charm_amount):
                dmg = (5+attack_charm_amount)
            elif player_roll >= (18-crit_charm_amount):
                dmg = (10+(attack_charm_amount*2))

            monster_HP -= dmg

            if player_roll <= (5-precision_charm_amount):
                type_text(f"You swing wildly! ... but it misses.")
            elif player_roll > (5-precision_charm_amount) and player_roll < (18-crit_charm_amount):
                type_text(f"You swing true and deal \033[31m{dmg}\033[m damage!")
            elif player_roll >= (18-crit_charm_amount):
                type_text(f"You swing by pure instinct! You deal \033[31m{dmg}\033[m damage!")
            
        elif player_choice == "b":
            player_roll = random.randint(1, 20) #Roll the dice!

            if player_roll <= (5-steadfast_charm_amount):
                defense = 0
            elif player_roll > (5-steadfast_charm_amount) and player_roll < (18-divine_blessing_amount):
                defense = (2+defence_charm_amount)
            elif player_roll >= (18-divine_blessing_amount):
                defense = (5+(defence_charm_amount*2))

            if player_roll <= (5-steadfast_charm_amount):
                type_text(f"You hold your Greatsword awkwardly to block and drop it ...")
            elif player_roll > (5-steadfast_charm_amount) and player_roll < (18-divine_blessing_amount):
                type_text(f"You make your grip firm and brace to block \033[31m{defense}\033[m damage!")
            elif player_roll >= (18-divine_blessing_amount):
                type_text(f"Your guard is on point! You block \033[31m{defense}\033[m damage!")
        
        elif player_choice == "h":
            heal_amt = (10+(healing_charm_amount*1.5))
            player_HP += heal_amt
            type_text(f"You drink a potion and recover \033[32m{heal_amt}\033[m HP.")
#----------------------------------------------------------------------------------------------------------------
        #Monster's turn
        if monster_HP <= 0:
            break

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
        zenny += random.randint(20,50)
        return True, zenny

#####
"""
1. I moved the decision down here so I can actually use the combat() function
2. I need to confirm that answering "n" will end the game and not just skip the combat, and that "y" will start the combat
"""
#####

result = None
if Decision_Kulu == "y": #I don't think there's any need for this to have a final else statment since the conditions above should cover it
    type_text(f"\n\033[36mVillage Chief:\033[m Great! I'll lead you to it right now!")
    
    #Loop for Kulu-Ya-Ku hunts
    while True:
        result, zenny = combat(name, "Kulu-Ya-Ku", 
                               zenny,
                               attack_charm_amount,
                               defence_charm_amount,
                               healing_charm_amount,
                               precision_charm_amount,
                               steadfast_charm_amount,
                               crit_charm_amount,
                               divine_blessing_amount)
        
        #Text depending on if you won or lost
        if result == True:
            print(f"You now have {zenny} zenny!")
            type_text(f"\n\033[32mYou defeated Kulu-Ya-Ku and earned some zenny!\033[m")
            
            #Ask if they want to visit the shop
            type_text("\033[1;35mWould you like to visit the shop? [y/n] >>>\033[m")
            visit_shop = input().strip().lower()
            while visit_shop not in ("y", "n"):
                type_text("\033[1;35mPlease enter a valid answer [y/n].\033[m\n")
                type_text("\033[1;35mWould you like to visit the shop? [y/n] >>>\033[m")
                visit_shop = input().strip().lower()
            
            if visit_shop == "y":
                zenny, attack_charm_amount, defence_charm_amount, healing_charm_amount, precision_charm_amount, steadfast_charm_amount, crit_charm_amount, divine_blessing_amount = shop(zenny,
                attack_charm_amount,
                defence_charm_amount,
                healing_charm_amount,
                precision_charm_amount,
                steadfast_charm_amount,
                crit_charm_amount,
                divine_blessing_amount)
            
            #Ask if they want to rehunt
            type_text("\033[1;35mWould you like to hunt Kulu-Ya-Ku again? [y/n] >>>\033[m")
            rehunt = input().strip().lower()
            while rehunt not in ("y", "n"):
                type_text("\033[1;35mPlease enter a valid answer [y/n].\033[m\n")
                type_text("\033[1;35mWould you like to hunt Kulu-Ya-Ku again? [y/n] >>>\033[m")
                rehunt = input().strip().lower()
            
            if rehunt == "n":
                break
        else:
            type_text(f"\n\033[36mVillage Chief:\033[m What a shame ... I really wanted to believe in you, but you're no hunter. Go back to wherever you came from!")
            sys.exit()
    
    #After Kulu-Ya-Ku sequence
    type_text(f"\n\033[36mVillage Chief:\033[m Impressive! You really are a hunter! Then I trust you to handle our bigger problem ...")
    type_text(f"\033[36mVillage Chief:\033[m The King of the Skies ... that damned \033[32mRathalos\033[m! It's been burning our crops and destroying nearby villages. Will you take care of it?")

elif Decision_Kulu == "n":
    type_text(f"\n\033[36mVillage Chief:\033[m Too scared? We don't need someone like you around, go back to wherever you came from!")
    sys.exit()

#Decision for Rathalos
type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
Decision_Rathalos = input()

#Ensures decision is valid
while Decision_Rathalos != "y" and Decision_Rathalos != "n":
    type_text("\033[1;35mPlease enter a valid answer from the options provided [y/n].\033[m\n")
    type_text("\033[1;35mDo you accept? [y/n] >>>\033[m")
    Decision_Rathalos = input()

#Choices based on decision
result = None
if Decision_Rathalos == "y":
    type_text(f"\n\033[36mVillage Chief:\033[m I knew you had it in you! Before you take it on, I would reccomend visiting our local shops.")
    
    #Loop for Rathalos hunts
    while True:
        zenny, attack_charm_amount, defence_charm_amount, healing_charm_amount, precision_charm_amount, steadfast_charm_amount, crit_charm_amount, divine_blessing_amount = shop(zenny,
        attack_charm_amount,
        defence_charm_amount,
        healing_charm_amount,
        precision_charm_amount,
        steadfast_charm_amount,
        crit_charm_amount,
        divine_blessing_amount)
        
        result, zenny = combat(name, "Rathalos", zenny,
                               attack_charm_amount,
                               defence_charm_amount,
                               healing_charm_amount,
                               precision_charm_amount,
                               steadfast_charm_amount,
                               crit_charm_amount,
                               divine_blessing_amount)
        
        #Text depending on if you won or lost
        if result == True:
            print(f"You now have {zenny} zenny!")
            type_text(f"\n\033[32mYou defeated Rathalos and earned some zenny!\033[m")
            
            #Ask if they want to visit the shop
            type_text("\033[1;35mWould you like to visit the shop? [y/n] >>>\033[m")
            visit_shop = input().strip().lower()
            while visit_shop not in ("y", "n"):
                type_text("\033[1;35mPlease enter a valid answer [y/n].\033[m\n")
                type_text("\033[1;35mWould you like to visit the shop? [y/n] >>>\033[m")
                visit_shop = input().strip().lower()
            
            if visit_shop == "y":
                zenny, attack_charm_amount, defence_charm_amount, healing_charm_amount, precision_charm_amount, steadfast_charm_amount, crit_charm_amount, divine_blessing_amount = shop(zenny,
                attack_charm_amount,
                defence_charm_amount,
                healing_charm_amount,
                precision_charm_amount,
                steadfast_charm_amount,
                crit_charm_amount,
                divine_blessing_amount)
            
            #Ask if they want to rehunt
            type_text("\033[1;35mWould you like to hunt Rathalos again? [y/n] >>>\033[m")
            rehunt = input().strip().lower()
            while rehunt not in ("y", "n"):
                type_text("\033[1;35mPlease enter a valid answer [y/n].\033[m\n")
                type_text("\033[1;35mWould you like to hunt Rathalos again? [y/n] >>>\033[m")
                rehunt = input().strip().lower()
            
            if rehunt == "n":
                break
        else:
            type_text(f"\n\033[36mVillage Chief:\033[m I... I can't believe you lost to the Rathalos. Perhaps you're not the one we needed after all.")
            sys.exit()
elif Decision_Rathalos == "n":
    type_text(f"\n\033[36mVillage Chief:\033[m ... you're no hunter, go back to wherever you came from!")
    sys.exit()




#####
""" 
The combat works well I just need to add some currency and shop system, so another function!
"""
#####


def shop(zenny,
         attack_charm_amount,
         defence_charm_amount,
         healing_charm_amount,
         precision_charm_amount,
         steadfast_charm_amount,
         crit_charm_amount,
         divine_blessing_amount):
    """Shop where the player can buy charms."""

    max_charm_amount = 3

    #Dictionary for charms
    charms = {
        "1": {"name": "Attack Charm", "cost": 10, "amount": attack_charm_amount},
        "2": {"name": "Defence Charm", "cost": 10, "amount": defence_charm_amount},
        "3": {"name": "Healing Charm", "cost": 10, "amount": healing_charm_amount},
        "4": {"name": "Precision Charm", "cost": 15, "amount": precision_charm_amount},
        "5": {"name": "Steadfast Charm", "cost": 15, "amount": steadfast_charm_amount},
        "6": {"name": "Crit Charm", "cost": 20, "amount": crit_charm_amount},
        "7": {"name": "Divine Blessing Charm", "cost": 25, "amount": divine_blessing_amount},
    }

    type_text("\033[1;35mWould you like to enter the shop? [y/n] >>> \033[m")
    decision_shop = input().strip().lower()

    while decision_shop not in ("y", "n"):
        type_text("\033[1;35mPlease enter a valid answer from the options provided [y/n].\033[m\n")
        type_text("\033[1;35mWould you like to enter the shop? [y/n] >>> \033[m")
        decision_shop = input().strip().lower()

    if decision_shop == "n":
        return (
            zenny,
            charms["1"]["amount"],
            charms["2"]["amount"],
            charms["3"]["amount"],
            charms["4"]["amount"],
            charms["5"]["amount"],
            charms["6"]["amount"],
            charms["7"]["amount"],
        )

    while True:
        type_text(f"\nWelcome to the shop, hunter! You have {zenny} zenny.\n")
        type_text("Please take a look at all the fine charms I have:\n")

        for key, charm in charms.items():
            type_text(
                f"{key}. {charm['name']} ({charm['cost']}) - Owned: {charm['amount']}/{max_charm_amount}\n"
            )

        type_text("8. Exit shop\n>>> ")
        player_choice = input().strip()

        while player_choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            type_text("\033[1;35mPlease enter a valid answer from the options provided [1/2/3/4/5/6/7/8].\033[m\n")
            type_text("8. Exit shop\n>>> ")
            player_choice = input().strip()

        if player_choice == "8":
            type_text("Come again soon, hunter!\n")
            break

        charm = charms[player_choice]

        if zenny < charm["cost"]:
            type_text("You do not have enough zenny.\n")
        elif charm["amount"] >= max_charm_amount:
            type_text(f"You already own the maximum number of {charm['name']}s.\n")
        else:
            charm["amount"] += 1
            zenny -= charm["cost"]
            type_text(f"You bought a {charm['name']}.\n")

    return (
        zenny,
        charms["1"]["amount"],
        charms["2"]["amount"],
        charms["3"]["amount"],
        charms["4"]["amount"],
        charms["5"]["amount"],
        charms["6"]["amount"],
        charms["7"]["amount"],
    )


#----------------------------------------------------------------------------------------------------------------
### Rathalos defeated, now Bloodbath Diablos decision and combat

#Text depending on if you won or lost against Rathalos
if result == True:
    print(f"This is your zenny {zenny}")
    type_text(f"\n\033[36mVillage Chief:\033[m Amazing! You truly are the greatest hunter I've ever seen!")
    type_text(f"\033[36mVillage Chief:\033[m But I must warn you... there is one last threat we face.")
    type_text(f"\033[36mVillage Chief:\033[m Deep in the Ancient Forest lurks the most terrifying creature known to mankind...")
    type_text(f"\033[36mVillage Chief:\033[m The \033[31mBloodbath Diablos\033[m. Will you face this ultimate challenge?\n")
else:
    type_text(f"\n\033[36mVillage Chief:\033[m I... I can't believe you lost to the Rathalos. Perhaps you're not the one we needed after all.")
    sys.exit()

#Decision if won against Rathalos
type_text("\033[1;35mDo you accept this final challenge? [y/n] >>>\033[m")
Decision_Bloodbath = input()

#Ensures decision is valid
while Decision_Bloodbath != "y" and Decision_Bloodbath != "n":
    type_text("\033[1;35mPlease enter a valid answer from the options provided [y/n].\033[m\n")
    type_text("\033[1;35mDo you accept this final challenge? [y/n] >>>\033[m")
    Decision_Bloodbath = input().strip().lower()

#Choices based on decision
if Decision_Bloodbath == "y":
    type_text(f"\n\033[36mVillage Chief:\033[m You are truly brave, hunter. One last visit to the shop before the final battle?")
    
    #Final loop for Bloodbath Diablos - allow retries
    while True:
        zenny, attack_charm_amount, defence_charm_amount, healing_charm_amount, precision_charm_amount, steadfast_charm_amount, crit_charm_amount, divine_blessing_amount = shop(zenny,
        attack_charm_amount,
        defence_charm_amount,
        healing_charm_amount,
        precision_charm_amount,
        steadfast_charm_amount,
        crit_charm_amount,
        divine_blessing_amount)
        type_text(f"\n\033[36mVillage Chief:\033[m The fate of Bherna Village rests on your shoulders now, hunter. Go forth and defeat the Bloodbath Diablos!")
        result, zenny = combat(name, "Bloodbath Diablos", zenny,
                               attack_charm_amount,
                               defence_charm_amount,
                               healing_charm_amount,
                               precision_charm_amount,
                               steadfast_charm_amount,
                               crit_charm_amount,
                               divine_blessing_amount)
        
        #Text depending on if you won or lost
        if result == True:
            break
        else:
            #Ask if they want to try again
            type_text("\033[1;35mWould you like to try the Bloodbath Diablos again? [y/n] >>>\033[m")
            retry = input().strip().lower()
            while retry not in ("y", "n"):
                type_text("\033[1;35mPlease enter a valid answer [y/n].\033[m\n")
                type_text("\033[1;35mWould you like to try the Bloodbath Diablos again? [y/n] >>>\033[m")
                retry = input().strip().lower()
            
            if retry == "n":
                type_text(f"\n\033[36mVillage Chief:\033[m No... the village is doomed...")
                type_text(f"\033[1;31mGame Over. Thank you for playing!\033[m\n")
                sys.exit()
elif Decision_Bloodbath == "n":
    type_text(f"\n\033[36mVillage Chief:\033[m I understand... but the village's fate will be sealed. Farewell, hunter.")
    sys.exit()

#----------------------------------------------------------------------------------------------------------------
### Ending based on final battle result

if result == True:
    type_text(f"\n\033[1;33m═══════════════════════════════════════════════════════════╪═══════════════════════════════════════════════════════════\033[m")
    type_text(f"\033[1;32mVICTORY!\033[m You have defeated the Bloodbath Diablos!")
    type_text(f"\033[1;33m═══════════════════════════════════════════════════════════╪═══════════════════════════════════════════════════════════\033[m")
    type_text(f"\n\033[36mVillage Chief:\033[m You've done it! The village is saved!")
    type_text(f"\033[36mVillage Chief:\033[m You are now a true legend among hunters. Your name will be remembered forever in Bherna Village.")
    type_text(f"\033[36mVillage Chief:\033[m Take this reward as a token of our eternal gratitude.\n")
    type_text(f"\033[1;32mYou have earned {zenny} Zenny from your incredible victories.\033[m")
    type_text(f"\033[1;32mThank you for playing, {name}! Your adventure has come to a triumphant end!\033[m\n")
else:
    type_text(f"\n\033[1;31m═══════════════════════════════════════════════════════════╪═══════════════════════════════════════════════════════════\033[m")
    type_text(f"\033[1;31mDEFEAT!\033[m The Bloodbath Diablos was too powerful...")
    type_text(f"\033[1;31m═══════════════════════════════════════════════════════════╪═══════════════════════════════════════════════════════════\033[m")
    type_text(f"\n\033[36mVillage Chief:\033[m No... it can't be. The village is doomed...")
    type_text(f"\033[36mVillage Chief:\033[m You fought valiantly, {name}, but the Bloodbath Diablos was simply too much for even you to handle.")
    type_text(f"\033[36mVillage Chief:\033[m We will remember your bravery forever.\n")
    type_text(f"\033[1;31mGame Over. Thank you for playing!\033[m\n")

