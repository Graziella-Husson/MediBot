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


class ActionSportDuration(Action):
	def name(self):
		return 'action_duration_sport'

	def run(self, dispatcher, tracker, domain):
		duration = tracker.get_slot("duration")
		tracker.update(SlotSet("sport_duration",duration))
		tracker.update(SlotSet("duration",None))

class ActionPainDuration(Action):
	def name(self):
		return 'action_duration_pain'

	def run(self, dispatcher, tracker, domain):
		duration = tracker.get_slot("duration")
		tracker.update(SlotSet("pain_duration",duration))
		tracker.update(SlotSet("duration",None))

class ActionSumUpPain(Action):
	def name(self):
		return 'sum_up_pain'
	
	def run(self, dispatcher, tracker, domain):
		pain_duration = tracker.get_slot("pain_duration")
		pain_level = tracker.get_slot("pain_level")
		body_part = tracker.get_slot("body_part")
		response = """To sum up, you have some {} pain localized at {} with a recurrence of {}.""".format(pain_level, body_part, pain_duration)
		dispatcher.utter_message(response)
		tracker.update(SlotSet("pain_duration",None))
		tracker.update(SlotSet("pain_level",None))
		tracker.update(SlotSet("body_part",None))
		
class ActionSumUpSport(Action):
	def name(self):
		return 'sum_up_sport'
	
	def run(self, dispatcher, tracker, domain):
		sport_duration = tracker.get_slot("sport_duration")
		sport_level = tracker.get_slot("sport_level")
		sport = tracker.get_slot("sport")
		response = """To sum up, you did some {} sport {} with a duration of {}.""".format(sport_level, sport, sport_duration)
		dispatcher.utter_message(response)
		tracker.update(SlotSet("sport_duration",None))
		tracker.update(SlotSet("sport_level",None))
		tracker.update(SlotSet("sport",None))
