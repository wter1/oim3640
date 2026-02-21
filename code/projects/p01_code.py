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

def type_text(text, delay=0.05, emphasis=1, pause=0.1):
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

if Decision_Kulu == "y": #I don't think there's any need for this to have a final else statment since the conditions above should cover it
    type_text(f"\n\033[36mVillage Chief:\033[m Great! I'll lead you to it right now!")
elif Decision_Kulu == "n":
    type_text(f"\n\033[36mVillage Chief:\033[m Too scared? We don't need someone like you around, go back to wherever you came from!")



#####
"""
1. I need to start creating the game options and figure out randomizer
"""
#####

