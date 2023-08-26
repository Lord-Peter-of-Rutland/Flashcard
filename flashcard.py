import random
## import flashcard_library_name

# User is asked to entre there firt name.
name = input("What is your first name? ")
# Greet the user
print("Good luck", name, "!")

# FLASHCARD GAME
finished = False
words = flashcard_library_name.list_name
# Amount of turns allowed
TURNS = int(input("How many questions would you like?"))

while !finished:
    # Choose a random command question from the "database" (dictionary)
    question = random.choice(words)
    #! Display the question to the user 
    # print question[0]?
    # Take the guess
    guess = input("Guess the command")

    # Use to log guesses
    guesses = []
    

    while TURNS > 0:
        if guess == question[1]:
            print("You are correct. Well done!")
            TURNS = TURNS - 1
            break
        else:
            # count the number of failures ??
            falied = 0
    