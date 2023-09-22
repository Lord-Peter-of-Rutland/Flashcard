# Library of questions for Flashcards
# CISCO ISO Commands
class flashcardLibrary():
    #! Change to storing  in a database
    cisco_iso_commands = {'Enter global config mode': 'configure terminal', 'Display current startup configuration' : 'show ruuning config',
        'Display current running configuration' : 'show running config'}
        
    def print_library(self):
        for key in self.cisco_iso_commands.keys():
            print(f"The question is {key} and the answer is {self.cisco_iso_commands[key]}")
            
    def add_question(self, question, answer):
        self.question_to_add = question
        self.answer_to_add = answer
        # Add to the database
        cisco_iso_commands.append(question, answer)
    
    def change_answer(self, correct_answer):
        pass
    
    def delete_question(self, question):
        pass
        # self.question_to_delete = 