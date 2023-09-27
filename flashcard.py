import random
from flashcard_library import flashcardLibrary     

class FlashcardGame():

    def __init__(self):
        self.flashcard_library = flashcardLibrary()
        question_library = self.flashcard_library.cisco_iso_commands
        self.questions = self.library.question_library.keys()
        
    # Start flashcard game
    def start_game(self):
        # Asks the user how many turns they should be allowed
        self.attempts = int(input("How many attempts for each questions would you like, 4 recogmended. >"))
        # User is asked to enter there first name.
        self.name = input("What is your first name? ")   
        self.number_of_questions = int(input("How many questions would you like?"))
        # To account for the edge case where someone inputs there answer capitalised I will be asking the user
        # to type there answer in all lower case.
        print(f"Hello {self.name}. Welcome to your terminal flashcard game")
        finished = False
        correct_guesses = []
        incorrect_guesses = []
        questions_to_ask = self.number_of_questions
        attempts_left = self.attempts
        while questions_to_ask != 0 or attempts_left == 0:
            # Choose a random question item from the "database" (dictionary)
            question = self.flashcard_library.random_qustion() #! Is this correct?
            answer = self.flashcard_library[question]
            print(question)
            guess = input("Guess the command >") #! trim the guess for spaces
            if guess == answer:
                print("You are correct. Well done!")
                correct_guesses.append(guess)
                questions_to_ask -= 1
                attempts_left = self.attempts
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
            print("Well done! You have finished with ", len(correct_guesses), " correct. And ", len(incorrect_guesses), " incorrect.")