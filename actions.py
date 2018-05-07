from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot
from rasa_core.events import SlotSet

class ActionSportLevel(Action):
	def name(self):
		return 'action_sport_level'
		
	def run(self, dispatcher, tracker, domain):
		tracker.update(SlotSet("sport_level","medium"))

