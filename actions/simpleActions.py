from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action

class Fallback(Action):
    def name(self):
        return 'sum_up_fallback'
        
    def run(self, dispatcher, tracker, domain):
        response = "Sorry, I did not understand what you said...\n`This is a fallback for NLU part (intent fallback)`"
        dispatcher.utter_message(response)

if __name__ == '__main__':
    print("aha")