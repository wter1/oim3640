"""
Creating something that can solve all possible words for the NYT Spelling Bee Puzzle.
A majority of this was done in the chapter 7 

Rule:
1. Uses only these 7 letters (Letters can repeat)
2. Must include the center letter (For this week ) 

"""


def check_word(word, available, required):
    """Check whether a word is acceptable.
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) >= 4 and uses_only(word, available) == True and uses_all(word, required) == True: #It would be redundant to make new conditional statements when we can just use the ones we already created
        return True
    return False

def score_word(word, available):
    """Compute the score for an acceptable word.
    
    >>> score_word('card', 'ACDLORT')
    1
    >>> score_word('color', 'ACDLORT')
    5
    >>> score_word('cartload', 'ACDLORT')
    15
    """


    if len(word) == 4:
        score = 1
    else:
        score = len(word)
    
    is_panagram = True
    for letter in available.lower():
        if letter not in word.lower():
            is_panagram = False
            break
    
    if is_panagram:
        score += 7 
    
    return score