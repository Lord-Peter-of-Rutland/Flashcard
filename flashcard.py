import random
#! Any comment with #! is an important read, also i have left code that may not work currently.
#! import flashcard_library_name

class FlashcardGame(flashcard_library_name):
    # Asks the user how many turns they should be allowed
    attempts = int(input("How many attempts for each questions would you like, 4 recogmended. >"))
    number_of_questions = int(input("How many questions would you like?"))
    # User is asked to enter there first name.
    name = input("What is your first name? ")
    # To account for the edge case where someone inputs there answer capitalised I will be asking the user
    # to type there answer in all lower case.
    print(f"Hello {name}. Welcome to your terminal flashcard game")
    # The library is taken from the imported library of questions
    #! Change to the actual list name
    flashcard_library = flashcard_library_name.list_name()
    
    # Start flashcard game
    def startGame(self):
        finished = False
        correct_guesses = []
        incorrect_guesses = []
        questions_to_ask = number_of_questions
        attempts_left = attempts
        while questions_to_ask != 0 or attempts_left == 0
            # Choose a random question item from the "database" (dictionary)
            question_answer = random.choice(flashcard_library)
            question = questions_answer[0] #! There is a better way of doing this. Instead take a random item from the list of keys and then access the dictonary with the key
            answer = questions_answer[1]
            print(question)
            guess = input("Guess the command >") #! trim the guess for spaces
            if guess == answer:
                print("You are correct. Well done!")
                correct_guesses.append(guess)
                questions_to_ask -= 1
                attempts_left = attempts
            else:
                incorrect_guesses.append(guess)
                attempts_left -= 1
                #! Check for permutations...
                # correct = False
                # i = 0
                # for c in guess:
                    # using a counter to iterate through the word to check the characters
                    # are correct.
                    # i += 1
                    # Instead of question[1] you need to iterate through the "ANSWER"
                    # if c == guess[i]:
                        # correct = True
            print("You finished with ", len(correct_guesses), " correct. And ", len(incorrect_guesses), " incorrect.")
