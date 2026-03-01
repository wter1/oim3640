# First Python App Proposal
### Core Skills
- Functions
- Logic
- User Interaction

### Idea 
~~I want to create a sort of "Choose your own adventure" app. It wouldn't have that much "functionality" other than being a source of entertainment, but I do think that it would cover all core skills listed above.~~

Ignore everything I said up there. After meeting with Professor Zhi, I've realized that just plain text would be pretty easy with a bunch of if statements and all that. I'm also not the best story creator, so instead I'll go with the idea he suggested of making an RPG. 

The RPG will be based off my favorite game franchise Monster Hunter! It still keeps some element of a "story" but that wouldn't be the focus. There will be **3** monsters to fight.

**Kulu-Ya-Ku:** This will be the beginner monster and sort of a tutorial to the combat system I'll create

**Rathalos:** This will be the "Final Boss" in the sense that the plot is that you've been dispatched to deal with this monster

**Bloodbath Diablos:** This is the "Secret Final Boss" which is just one of my favorite monsters

The combat will be dependent on the "random" library. I want to make a sort of d20 dice for attacks on both ends of the spectrum (Monsters and the user). My current idea is anything less than some value (probably base 5) will be a wiffed attack and do no dmg. Anything greater than some value (probably 18) will be a critical attack. To reduce the chance aspect of the game and improve odds, I'll add some store system that will change the items you have so they can either reduce the number needed to wiff or reduce the number needed to crit.

I want monsters to have at least 5 attacks, but that might be too ambitious for me so I may reduce it to 3 or something similar. In the same vein monsters can wiff and crit just like hunters, but instead of items, the chance of either will be dependet on how difficult the monster is. Kulu-Ya-Ku will be 1 star of difficulty, Rathalos will be 5 stars and Bloodbath Diablos will be 10 stars. I'll map out how the different stars affect the odds of the monsters rolls later.

There are 14 weapons in the real game, but to make things simple, the only weapon the user will be given is a greatsword. 

I may add more monsters if 3 seems to small of a batch. 


### After Session 11


- Names can't have spaces right now. I need to fix thaty


### Vague Areas (From AI)

**Game flow & user interface**

*How does the player navigate? Turn-by-turn prompt? Menu choices?
What constitutes “winning” or “losing”? Will you have health bars, potions, etc.?*

The main player loop will be a turn by turn prompt. With intermediary sections that shows the aftermath of an action (Health points left for player and monster).


**Combat mechanics details**

*You mention ranges (<5 wiff, >18 crit) but not the overall die size (d20? d100?).
How are damage values calculated? Fixed, random, based on weapon/monster stats?*

It will be a d20 dice and the damage values or number values in general will be fixed

**Inventory/store system**

*What items exist? How do they modify odds (e.g. “+2 to hit”, “–1 to wiff”)?
How does the player earn currency? Is there a shop menu or pre‑battle load‑out?*

Item's will exist as charms that you can buy from some shop menu and yes they will be additive and subtractive modifications.

**Monster behavior**

*Will monsters choose attacks randomly, or have patterns?
How does difficulty map to odds (“1 star = x% crit chance, 10 stars = y%”)?
Do monsters have health or stages?*

I want to implement a pattern, but just to start off, a random choice between options should work. I might scrap the star idea since how difficult the monster is kind of depends on how I 

Data structures & organization

How will you represent monsters/weapons/items? Dictionaries? Classes?
Error handling & input validation

You already discovered an issue with spaces in names; what other edge cases might there be?
“Story” or context

Currently there’s only a loose plot (“dispatched to deal with Rathalos”); is there any narrative between fights or an ending screen?