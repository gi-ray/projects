import random

def diceRoll():
    
    counter = 0
    while True:
        roll = input("Do you want to roll the dice (y/n)?: ").lower()
        if roll == "y":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            count = input("How many times do you want to roll the dice? ")
            if count == "1":
                print(f"{dice1}")
                counter += 1
            if count == "2":
                print(f"{dice1}, {dice2}")
                counter += 1
            if count != "1" and count != "2":
                print("Invalid  input")
        if roll == "n":
                    print("You did not roll the dice.")
                    print("You rolled the dice", counter, "times")
                    break
diceRoll()