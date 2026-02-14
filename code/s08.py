"""
Notes:
Not 100 lines of code, just something you're proud of
*Your first Python App*
    I think I'll try to make some kind of visual novel or a kind of choose your own adventure!

Decomposition
Abstraction

Testing at each step just to see if your code works 
Calling other functions


"cls" clears terminal


When would you use nested conditionals? 
When the conditions of what you're checking will be different
"""

# print(0.1+0.2)



# def fun(x):
#     print("hello world")
#     return x


# y = 5 + fun(5)

# print(y)

# age = int(input("What is your age?  >>"))

# if age < 21:
#     print("No you cannot.")
# elif age > 65:
#     print("You are too old for this!")
# else: 
#     print("Yes, you can.")

score = int(input("What is your raw grade? >>"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
