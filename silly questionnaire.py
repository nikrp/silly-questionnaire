'''

    My program prints out a quiz that has three questions. It then checks if the question is correct or wrong. If it is wrong, it adds it to a variable which
will then be printed out at the end as a score.

'''
print("Today, I am going to give you a quiz on easy stuff, it is three questions. Make sure you add your name!")
name = input("Name: ")
wrongCounter = 0
questionOne = int(input("What is X, if X + 7843518734560 = 7843518734561? "))
if questionOne == 7843518734561 - 7843518734560:
    print("Correct!!!")
else:
    print("Wrong!!!")
    wrongCounter += 1

questionTwo = int(input("What is 30 + 30? "))
if questionTwo == 30 + 30:
    print("Correct!!!")
else:
    print("Wrong!!!")
    wrongCounter += 1

questionThree = int(input("What is 7 * 8/28 + 14? Remember to use the order of operations! "))
if questionThree == 7*8/28+14:
    print("Correct!!!")
else:
    print("Wrong!!!")
    wrongCounter += 1

if wrongCounter == 0:
    print(f'Hey {name}, You Passed!!')
elif wrongCounter == 3:
    print("Hard Luck, You Failed College...")
else:
    print(f"Hey {name}, Only {wrongCounter} Wrong! Great Job!")

print("Great job everyone!!! I hope I see you all again!")
