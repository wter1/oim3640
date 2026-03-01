def uppercheck(word):
    for letter in word:
        if letter.isupper():
            return True
    return False


print(uppercheck("iPhone"))

print(uppercheck("Babson"))
