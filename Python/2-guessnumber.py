import random

def guessNumber():
    guessed = False
    min = int(input("Enter a minimum number: "))
    max = int(input("Enter a maximum number: "))
    number = random.randint(min, max)
    tries = 0
    invalid = False
    while guessed == False:
        guess = int(input("Guess a number between " + str(min) + " and " + str(max) + ": "))
        if guess < min or guess > max:
            invalid == True
            print("Invalid number!")
            break
        while guess != number and invalid == False:
            tries += 1
            if guess > number:
                print("Too high!")
                break
            if guess < number:
                print("Too low!")
                break
        if guess == number:
            tries += 1
            print("You guessed the number in " + str(tries) + " tries!")
            guessed == True
            break
        if tries == 5:
            print("You ran out of tries.\n The number was: ", number)
                  
                
            
guessNumber()         