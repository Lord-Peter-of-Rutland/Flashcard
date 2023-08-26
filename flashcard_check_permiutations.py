import random
# Importing the library we need in order to make a random choise
# Flashcard, check permutations of the word

# User is asked to entre there firt name.
name = input("What is your first name? ")
# Greet the user
print("Good luck", name, "!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

cisco_commands = {"A configuration mode command that sets this Cisco device password that is required for any user to enter enable mode" : "enable secret"}

# choose a random command from the theosaurus
word = random.choice(words)
print("Guess the command")

guesses = []

# amount of turns to guess
turns = 12

while turns > 0:

    # counting the number of failures
    failed = 0

    # !Important! Need to check each character within the word against every
    # char within guesses. 
    # if the word equals the guesses EXACTLY you win. Change so that it can check permutations of the word
    if word == guesses:
        print("You win!")
        break

    # checking all characters from the chosen word
    # letter taken one at a time
    for char in word:

        # comparing the character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")

        # increment 1 for every failure
        failed += 1

    if failed == 0:
        # user wins if 0, You win given as output
        print("You Win!")

        # print the word that was correct
        print("The word is: ", word)
        break

    # if the letter is not within the word ask user for another
    print()
    guess = input("Guess a character:")

    # Every input guess wil be entered into guesses 
    guesses += guess

    # Check the input with the letter in the word
    if guess not in word:

        turns -= 1

        # If the character doesnt match the word
        # Display Wrong to the user
        print("Wrong letter")

        # Print the number of turns left to the user
        print("You have ", turns, " guesses left")

        if turns == 0:
            print("You Loose...")
            # print("Would you like to try again?")
            # IF THE NEW WORD IS THE SAME AS LAST WORD = NEW.RANDOM.WORD
            ## FIND A WAY OF RESETTING THE TERMINAL




