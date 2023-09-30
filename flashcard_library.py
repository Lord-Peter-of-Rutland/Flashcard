# Library of questions for Flashcards
# CISCO ISO Commands
import random

class flashcardLibrary():
    #! Change to storing  in a database
    def __init__(self):
        self.cisco_iso_commands = {'Enter global config mode': 'configure terminal', 'Display current startup configuration' : 'show runing config',
        'Display current running configuration' : 'show running config'}
    
    def random_question(self):
        questions = self.cisco_iso_commands.keys()
        question = random.choices(list(questions))
        return question
    
    def print_library():
        questions = flashcardLibrary.cisco_iso_commands.keys()
        for key in questions:
            print(f"The question is {key} and has the answer {flashcardLibrary.cisco_iso_commands[key]}" , " is this correct?")
           
    def add_question(self, question, answer):
        self.question_to_add = question
        self.answer_to_add = answer
        # Add to the database
        self.cisco_iso_commands.pop(question, answer)
    
    def change_answer(self, correct_answer):
        pass
    
    def delete_question(self, question):
        pass
        # self.question_to_delete = 