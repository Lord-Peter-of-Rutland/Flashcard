# Library of questions for Flashcards
# CISCO ISO COMMANDS
class CISCO_Commands():
    #! Change to storing  in a database
    cisco_iso_commands = {'Entre global config mode': 'configure terminal', 'Display current startup configuration' : 'show ruuning config',
        'Display current running configuration' : 'show running config'}
        
        def print_library()
            for key in self.cisco_iso_commands:
                print(f"The question is {key} and the answer is {cisco_iso_commands[key]})
                
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