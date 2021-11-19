########## number guessing game python ###########
import random
def GuessingNumberGame():
    userGuess = 0
    count = 0
    number = random.randint(1 , 10)
    while userGuess != number:
        userGuess = int(input("Enter Number 1 to 10 = "))
        count += 1
        
        if userGuess == number:
            print("You Won")
            print("The number of your guesses is %s"% (count))
            break
        
        elif userGuess < number:
            print("Your Number is low")

        elif userGuess > number:
            print("Your Number is high")
        

GuessingNumberGame()
