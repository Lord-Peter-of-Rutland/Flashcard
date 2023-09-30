import unittest
# Functional Test for the Flashcard app
# The application is started with the library of questions added and checked that it functions correctly
from flashcard_library import flashcardLibrary
import flashcard

class NewFlashcardGame(unittest.TestCase):
    # The user Mickae opens the flashcard game in python, with the argument of the library he wants to use
    def setUp(self):
        self.library = flashcardLibrary()
        question =  self.library.random_question()
        self.assertNotEqual(question, None, "There was a question...")
        

    def test_has_a_library_of_questions(self):
        self.assertNotEqual(None, self.library.print_library())
        self.assertIn("Enter global config mode", self.library.print_library(), "The first question is not in the library")
            
    # He is greeted with a welcome that asks his name
    # after entering the name, he is asked how many questions he would like, Steven enters 5
    def test_starting_a_game(self):
        self.game = flashcard()
        self.start_game = self.game.start_game()
    # after hitting enter Steven is given a question in the terminal and is asked to answer it.

    # the attempt is saved
    # the number of ATTEMPTS is decreased 
    # the attempt is checked against the answer.
    # If correct, Steven is given a congratualtions message.

    # The next question is asked and the number of questions to ask is reduced.
    # The number of ATTEMPTS allowed is reset.

    # Once all the questions are asked, Steven is given a summery of the game.
    # With the number of attempts and the wrong answers
    # Steven is asked wether he would like to re-attempt the questions he got incorrect.

    # If Steven runs out of attempts, he is asked if he would like to continue.
    # If yes, the number of attempts resets for that question. Otherwise the app exits.

if __name__ == '__main__':
    unittest.main()
