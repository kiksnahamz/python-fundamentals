'''
Number guessing game.
First, user selects whether or not they want to play by inputting Y or n
User inputs a number, which is checked to see if it is between 1 and 100
If so, this is then compared a randomly generated number between 1 and 100
The user is then alerted whether they guessed correctly or, if wrong, told by how much they missed
'''


import random

number = random.randrange(1,100,1)
user_input = input("Enter 'y' if you would like to play: ")
while True:
    user_number = int(input("Guess a number between 1 and 100: "))
    if user_input in ("y", "Y"):
        if 1 <= user_number <= 100:
            if user_number == number:
                print("You guessed correctly!")
            else:
                print(f"Sorry, it's wrong!, the real number is {number}, you were only {abs(number - user_number)} spaces out")
        else:
            print("Sorry the number that you entered wasn't between 1 and 100. Try again")
