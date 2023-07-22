import csv
import random


print("Welcome to the Vocab Game!")
print("")

# Pick random row index
randomNumbersSet = set()

while len(randomNumbersSet) < 4:
  randomNumbersSet.add(random.randint(2, 14))

randomNumbersList = list(randomNumbersSet)

# Generate Answer Options

rightAnswer = []
altAnswer1 = []
altAnswer2 = []
altAnswer3 = []

with open("./vocab.csv", 'r') as file:
  vocabList = csv.reader(file)
  for i, row in enumerate(vocabList, start=1):
    if i in (randomNumbersList):
      if len(rightAnswer) == 0:
        rightAnswer.append(row)
      elif len(altAnswer1) == 0:
        altAnswer1.append(row)
      elif len(altAnswer2) == 0:
        altAnswer2.append(row)
      elif len(altAnswer3) == 0:
        altAnswer3.append(row)

answerOptions = [(rightAnswer[0])[0], altAnswer1[0][0], altAnswer2[0][0], altAnswer3[0][0]]
random.shuffle(answerOptions)


# Output the question

print("The defintion is:", (rightAnswer[0])[1])
print('')
for i, answer in enumerate(answerOptions, start=1):
    print(f"{i}. {answer}")

#Get User input

userChoice = input("Your Answer is (1-4): ")
print("")
while userChoice == '' or userChoice not in ('1', '2', '3', '4'):
  userChoice = input("Please choose a valid answer: (1-4) ")

userChoice = int(userChoice)
#Answer Validation

if(answerOptions[userChoice - 1] == (rightAnswer[0])[0]):
  print('Congratulations! You got the right answer')
else:
  print(f"{answerOptions[userChoice - 1]} is not the right answer. The correct answer is: {rightAnswer[0][0]}")
print("")
print(f"{answerOptions[userChoice - 1]} means ")


