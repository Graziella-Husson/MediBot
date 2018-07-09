from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from ressources import get_utterance

class Fallback(Action):
    def name(self):
        return 'sum_up_fallback'
        
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        response = get_utterance("fallback",language)
        dispatcher.utter_message(response)

if __name__ == '__main__':
    print(get_utterance("fallback","en"))