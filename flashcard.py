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
    q_and_a = random.choice(words)
    question = q_and_a[0] # CHECK THE OUTPUT
    answer = q_and_a[1]
    #! Display the question to the user 
    # print question[0]?
    # Take the guess
    guess = input("Guess the command")

    # Use to log guesses
    guesses = []
    

    while TURNS > 0:
        #! Does't account for permutations
        guesses.append(guess)
        if guess == answer
            print("You are correct. Well done!")
            TURNS -= 1
            break
        else:
            # count the number of failures ??
            falied += 1
        # Check for permutations...
        correct = False
        i = 0
        for c in guess:
            # using a counter to iterate through the word to check the characters
            # are correct.
            i += 1
            # Instead of question[1] you need to iterate through the "ANSWER"
            if c == :
                correct = True
    
    