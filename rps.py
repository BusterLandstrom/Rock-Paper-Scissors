#Set Values that should not be updated every rond (only in the beggining)
import time
import random
lives = 10
compLives = 10
winAmmount = 0
tieAmmount = 0
lossAmmount = 0
optionsArray = ["rock", "paper", "scissors"]
numOptionsArray = [1,2,3]
chosenOption = 0
resultArray = ["Tie","Win","Lose"]
matchCounter = 0
while True:

    #Starting all variables for each round
    isDone = False
    result = 0
    compSetAnswer = ""

    #Player choses option
    option = input("What option will you choose? Rock, Paper, Scissors or Exit\n").lower()

    #Translate the option into a number (I know i could do this more efficient but i dont care)
    if option == "rock":
        chosenOption = 1
    elif option == "paper":
        chosenOption = 2
    elif option == "scissors":
        chosenOption = 3
    elif option == "exit":
        print("You forfeited " + "\nIt took " + str(matchCounter) + " matches to forfeit\nWins: " + str(winAmmount) + "\nTies: " + str(tieAmmount) + "\nLosses: " + str(lossAmmount))
        txtFile = open("results.txt","w") 
        inputTxt = ["Matches: " + str(matchCounter) + "\nWins: " + str(winAmmount) +" \nLosses: " + str(lossAmmount) + "\nTies: " + str(tieAmmount)]
        txtFile.writelines(inputTxt) 
        txtFile.close()
        exit()
    else:
        chosenOption = 4

    #Computer choses its option.
    compAnswer = random.choice(numOptionsArray)

    #Computer chosing loading screen
    bar = [
        "<('o'<)",
        "(>‘o’)>",
        "<('o'<)",
        "(>‘o’)>",
        "<('o'<)",
        "(>‘o’)>"
    ]
    i = 0
    while isDone == False:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.4)
        i += 1
        if i == 4:
            isDone = True

    #Changing the computer option to text for use later
    if compAnswer == numOptionsArray[0]:
        compSetAnswer = "rock"
    elif compAnswer == numOptionsArray[1]:
        compSetAnswer = "paper"
    elif compAnswer == numOptionsArray[2]:
        compSetAnswer = "scissors"

    #Checking what the result will be accoring to what you and the computer chose
    if chosenOption == compAnswer:
        result = 1
    elif chosenOption == numOptionsArray[0]:
        if compAnswer == numOptionsArray[1]:
            result = 3
        if compAnswer == numOptionsArray[2]:
            result = 2
    elif chosenOption == numOptionsArray[1]:
        if compAnswer == numOptionsArray[0]:
            result = 2
        if compAnswer == numOptionsArray[2]:
            result = 3
    elif chosenOption == numOptionsArray[2]:
        if compAnswer == numOptionsArray[0]:
            result = 3
        if compAnswer == numOptionsArray[1]:
            result = 2
    else:
        result = 4

    #Changing values depending on what the result is and also chosing what result is what
    if result == 1:
        print("It was a tie.\nYou chose " + str(option) + " and your opponent chose " + str(compSetAnswer) + "\nLives: " + str(lives) + "\n")
        tieAmmount += 1
        matchCounter += 1
    elif result == 2:
        print("You won.\nYou chose " + str(option) + " and your opponent chose " + str(compSetAnswer) + "\nLives: " + str(lives) + "\n")
        winAmmount += 1
        lives += 1
        compLives += -1
        matchCounter += 1
    elif result == 3:
        print("You lost.\nYou chose " + str(option) + " and your opponent chose " + str(compSetAnswer) + "\nLives: " + str(lives) + "\n")
        lossAmmount += 1
        lives += -1
        compLives += 1
        matchCounter += 1
    elif result == 4:
        print("Incorrect answer try again\n")

    #Checking if you succed in beating the computer or lose
    if compLives < 1:
        print("YOU ARE THE CHAMPION CONGRATULAITONS\nIt took " + str(matchCounter) + " matches to win\nWins: " + str(winAmmount) + "\nTies: " + str(tieAmmount) + "\nLosses: " + str(lossAmmount))
        txtFile = open("results.txt","w") 
        inputTxt = ["Matches: " + str(matchCounter) + "\nWins: " + str(winAmmount) +" \nLosses: " + str(lossAmmount) + "\nTies: " + str(tieAmmount)]
        txtFile.writelines(inputTxt) 
        txtFile.close()
        exit()
    elif lives < 1:
        print("You lost better luck next time!\nIt took " + str(matchCounter) + " matches to lose\nWins: " + str(winAmmount) + "\nTies: " + str(tieAmmount) + "\nLosses: " + str(lossAmmount))
        txtFile = open("results.txt","w") 
        inputTxt = ["Matches: " + str(matchCounter) + "\nWins: " + str(winAmmount) +" \nLosses: " + str(lossAmmount) + "\nTies: " + str(tieAmmount)]
        txtFile.writelines(inputTxt) 
        txtFile.close()
        exit()

#Copyright © Viktor Landström 2019
#P.S I will build separate methods for each step