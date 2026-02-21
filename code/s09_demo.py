# for i in range(5):
#     print(i)

# import time

# i = 0
# while i < 5:
#     print(i)
#     time.sleep(1)
#     i += 1

# response = ""
# while response != "quit": #This can be like a terminal (You want the user to keep doing things before quitting)
#     response = input("Enter command: ")
#     print(f"You said: {response}") 



# print("\n--- Simple Login System ---")
# username = input("Enter username: ")
# password = input("Enter password: ")

# while True:
#     if username == "admin" and password == "password123":
#         print("Login successful! Welcome, admin.")
#         break
#     else:
#         print("Invalid credentials. Please try again.")
#         username = input("Enter username: ")
#         password = input("Enter password: ")


#Break statement is used to exit a loop.


# words = ["apple", "banana", "cherry", "date", "elderberry"]
# for w in words:
#     print('checking word:', w)
#     if w == "cherry":
#         print("Found it!\n")
#         continue
#     print("Not this one.\n")

#Continue statement is used to skip the current iteration of a loop and move to the next one.
for num in range(10):
    if num % 2 == 0:
        continue
    print(num) #prints odd numbers only

#Return can only be used in a function

