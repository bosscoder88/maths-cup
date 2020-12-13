#### Startup ##
import random
from time import sleep as s
names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
thirdPlace = []
##for x in range(1, 33):
##    print("Name", x)
##    name = input("Please enter a name: ")
##    names.append(name)
#print(names) ## This line is for bug fixing, uncomments if you want to check all the names are in the list.


print("Welcome to Maths Cup!")
print("Today, the rounds will be as follows:\n")
print("""Round 1: Multiplication
Round 2: Division
Quarter Final: Bidmas
Semi Final: HCF and LCM
Third place/Final: Mean\n\n\n""")


s(5)
######################################
######################## Round 32 ####
######################################
print("Round 32")
for x in range(1, 17):
    random.shuffle(names)
    print("""==========
Question""", x, "\n==========")
    no1 = random.randint(15, 50)
    no2 = random.randint(10,30)
    p1 = names[0]
    players = int(len(names))
    player = int(players - 1)
    p2 = names[player]
    print(p1, "is player 1, and", p2, "is player 2!")
    
    input("Please press enter when you are ready to recieve your question.\n")
    print("##########################\n")
    print("Your question is:", no1, "x", no2, "\n")
    print("##########################\n")
    won = int(input("Please type either 1 or 2 depending on who won the round. "))
    print("\nThe correct answer was indeed", no1*no2)
    if won == 1:
        del names[player]
        print("\nCongratulations,", p1, "!")
        print("Better luck next time,", p2, "!\n\n")
    if won == 2:
        del names[0]
        print("Congratulations,", p2, "!")
        print("Better luck next time,", p1, "!\n\n")
print("Who's made it through to the next round?")
for x in names:
    print(x)
s(5)    
######################################
######################## Round 16 ####
######################################
    
print("\n\n\nRound 16!")
print("For this round, please round your answers to 2 d.p. where necessary.")
for x in range(1, 9):
    random.shuffle(names)
    print("""==========
Question""", x, "\n==========")
    no1 = random.randint(15, 50)
    no2 = random.randint(4,12)
    p1 = names[0]
    players = int(len(names))
    player = int(players - 1)
    p2 = names[player]
    print(p1, "is player 1, and", p2, "is player 2!")
    
    input("Please press enter when you are ready to recieve your question.\n")
    print("##########################\n")
    print("Your question is:", no1, "÷", no2, "\n")
    print("##########################\n")
    won = int(input("Please type either 1 or 2 depending on who won the round. "))
    print("\nThe correct answer was indeed", no1/no2)
    if won == 1:
        del names[player]
        print("\nCongratulations,", p1, "!")
        print("Better luck next time,", p2, "!\n\n")
    if won == 2:
        del names[0]
        print("Congratulations,", p2, "!")
        print("Better luck next time,", p1, "!\n\n")
print("Who's made it through to the next round?")
for x in names:
    print(x)
s(5)
######################################
################### Quarter Final ####
######################################
    
print("\n\n\nQuarter Final!")
for x in range(1, 5):
    random.shuffle(names)
    print("""==========
Question""", x, "\n==========")
    no1 = random.randint(15, 50)
    no2 = random.randint(4, 12)
    no3 = random.randint(10, 20)
    p1 = names[0]
    players = int(len(names))
    player = int(players - 1)
    p2 = names[player]
    print(p1, "is player 1, and", p2, "is player 2!")
    
    input("Please press enter when you are ready to recieve your question.\n")
    print("##########################\n")
    print("Your question is:", no1, "-", no2, "x", no3, "\n")
    print("##########################\n")
    won = int(input("Please type either 1 or 2 depending on who won the round. "))
    print("\nThe correct answer was indeed", no1-no2*no3)
    if won == 1:
        del names[player]
        print("\nCongratulations,", p1, "!")
        print("Better luck next time,", p2, "!\n\n")
    if won == 2:
        del names[0]
        print("Congratulations,", p2, "!")
        print("Better luck next time,", p1, "!\n\n")
print("Who's made it through to the next round?")
for x in names:
    print(x)
s(5)

######################################
###################### Semi Final ####
######################################
    
print("\n\n\nSemi Final!")
for x in range(1, 3):
    random.shuffle(names)
    print("""==========
Question""", x, "\n==========")
    numbers1 = ["4", "6", "8", "10", "12", "14", "16", "18", "20", "24"]
    numbers2 = ["8", "18", "36", "40", "28", "32", "54"]
    no1 = random.choice(numbers1)
    no2 = random.choice(numbers2)
    p1 = names[0]
    players = int(len(names))
    player = int(players - 1)
    p2 = names[player]
    print(p1, "is player 1, and", p2, "is player 2!")
    
    input("Please press enter when you are ready to recieve your question.\n")
    print("##########################\n")
    print("Please find the HCF and LCM of these numbers:", no1, "and", no2)
    print("\n##########################\n")
    won = int(input("Please type either 1 or 2 depending on who won the round. "))
    ###
    number1 = int(no1)
    number2 = int(no2)
    temp1 = number1
    temp2 = number2
    while temp2 != 0:
    	t = temp2
    	temp2 = temp1%temp2
    	temp1 = t
    hcf = temp1
    lcm = (number1*number2)/hcf
    print("The HCF was", hcf, "and the LCM was", lcm, "\n\n")
    if won == 1:
        thirdPlace.append(p2)
        del names[player]
        print("\nCongratulations,", p1, "!")
        print("Better luck next time,", p2, "!\n\n")
    if won == 2:
        thirdPlace.append(p1)
        del names[0]
        print("Congratulations,", p2, "!")
        print("Better luck next time,", p1, "!\n\n")
print("Who's made it through to the next round?")
for x in names:
    print(x)
print("\nHowever, this time, these people made it to the 3rd place round!")
for entry in thirdPlace:
    print(entry)
s(5)

######################################
############## 3rd place play-off ####
######################################
    
print("\n\n\n3rd Place play-off!")
random.shuffle(names)
print("""==========
Question 1
==========""")
numbers = []
for x in range(1,10):
    numbers.append(random.randint(2, 14))
    #print(numbers) ## again this is for debugging, uncomment to check the list of numbers.
p1 = thirdPlace[0]
players = int(len(thirdPlace))
player = int(players - 1)
p2 = thirdPlace[player]
print(p1, "is player 1, and", p2, "is player 2!")

input("Please press enter when you are ready to recieve your question.\n")
print("##########################\n")
print("Please find the mean of this sequence:")
for entry in numbers:
    print(entry, end=', ')
print("\n\n##########################\n")
won = int(input("Please type either 1 or 2 depending on who won the round. "))
print("\nThe correct answer was indeed", sum(numbers)/len(numbers))
if won == 1:
    print("\nCongratulations,", p1, "!  You are third place in today's Maths Cup!")
    print("Better luck next time,", p2, "!\n\n")
if won == 2:
    print("Congratulations,", p2, "! You are third place in today's Maths Cup!")
    print("Better luck next time,", p1, "!\n\n")
print("Let's go to the final and see", names[0], "and", names[1], "battle it out!")
s(5)

######################################
####################### The Final ####
######################################
    
print("\n\n\nWelcome to the final!\n")
print("""In the final, there will be 3 questions.
Whoever gets two of those questions correct will be the winner of today's Maths Cup.\n""")
random.shuffle(names)
p1won = 0
p2won = 0
for x in range(1, 4):
    print("""==========
Question""", x, "\n==========")
    numbers = []
    for x in range(1,10):
        numbers.append(random.randint(2, 14))
    p1 = thirdPlace[0]
    players = int(len(thirdPlace))
    player = int(players - 1)
    p2 = thirdPlace[player]
    print(p1, "is player 1, and", p2, "is player 2!")
    
    input("Please press enter when you are ready to recieve your question.\n")
    print("##########################\n")
    print("Please find what the mean is in this sequence:")
    for entry in numbers:
        print(entry, end=', ')
    print("\n\n##########################\n")
    won = int(input("Please type either 1 or 2 depending on who won the round. "))
    print("\nThe correct answer was indeed", sum(numbers)/len(numbers))
    if won == 1:
        p1won = p1won + 1
        if p1won < 2:
            print("Congratulations", p1, ", you have now won", p1won, "games!")
            print("You can still catch up", p2, ", you have won", p2won, "games!")
        elif p1won == 2:
            print("Congratuations", p1, "you have just won today's Maths Cup!")
    if won == 2:
        p2won = p2won + 1
        if p2won < 2:
            print("Congratulations", p2, ", you have now won", p2won, "games!")
            print("You can still catch up", p1, ", you have won", p1won, "games!")
        elif p2won == 2:
            print("Congratuations", p2, "you have just won today's Maths Cup!")
