'''
    1. Open a questions file and save it in a variable.
    2. Generate a number between one and the number of questions.
    3. Print the question.
    4. Open the answer file.
    5. Print the answer for the question he asked.
    6. Ask him more questions.
'''
import random

# Open the question file and read it into array
qFile = open(r"questions.txt", 'r')
qList = qFile.readlines()
#print(qList); Temp

#Open answer file
aFile = open(r"answers.txt", 'r')
aFileList = aFile.readlines()

correctCount = 0
totalCount = int(input("How many questions do you want to answer?: "))

for i in range(0, totalCount):
    # Generate the num 0-19 and display that question
    num = random.randint(0, 36)
    theirAnswer = input(qList[num])
    #print(theirAnswer) #Temp

    #split line num to array
    aList = aFileList[num].strip().split(';')
    #print(aList) #Temp

    # Check for answer
    if theirAnswer.lower() in aList:
        print("Correct!!!")
        correctCount += 1
    else:
        print("Nice Try!")

print(correctCount)
passPercentage = (correctCount/totalCount)*100
roundingPercent = round(passPercentage, 2)
print(f"Your score is {roundingPercent}%! Great job!")
    
#cleanup before exit
qFile.close()
aFile.close()
