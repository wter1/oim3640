score = int(input("Enter your score: \n"))

if score >= 60:
    print("Congratulations! You passes the exam.")
elif score >= 90:
    print("Excellent work! You scored an A.")
else:
    print("Unfortunately, you didd no pass. Better luck next time.")



if score >= 90:
    print("Excellent work! You scored an A.")
elif score >= 60:
    print("Congratulations! You passes the exam.")
else:
    print("Unfortunately, you didd no pass. Better luck next time.")


def evaluate_score(score):
    if score >= 90:
        print("Excellent work! You scored an A.")
    elif score >= 60:
        print("Congratulations! You passes the exam.")
    else:
        print("Unfortunately, you didd no pass. Better luck next time.")

#Alt + direction key = changes the position of the line

score = int(input("Enter your score: "))
result = evaluate_score(score)
print(result)

#If you dont want to add a file to public use gitignore (Literally go to gitignore and put the file directory into it)
#def main is the entry point of the whole code (The random caller professor made in class)

#Precendence of python operators

#Rule of thumb: If you know the count, use for. if you're waiting for a condition, use while.

#Initialize variables also called a flag variable




