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
		pain_change = tracker.get_slot("pain_change")
		period = tracker.get_slot("period")
		if pain_duration == None:
			response = "How long did you have this pain?\nDEBUG : from action"
		elif pain_level == None:
			response = "I did not recognize any description of your pain. Can you tell me more about it? (e.g. is it a sharp pain?).\nDEBUG : from action"
		elif body_part == None:
			response = "Where is localized this pain?\nDEBUG : from action"
		else:
			response = """To sum up, you have some {} pain localized at {} with a duration of {}. The pain seems to be {}\nDEBUG : \n\tperiod : {}\n""".format(pain_level, body_part, pain_duration, pain_change, period)
			tracker.update(SlotSet("pain_duration",None))
			tracker.update(SlotSet("pain_level",None))
			tracker.update(SlotSet("body_part",None))
			tracker.update(SlotSet("pain_change",None))
		dispatcher.utter_message(response)
		

class ActionSumUpSport(Action):
	def name(self):
		return 'sum_up_sport'
	
	def run(self, dispatcher, tracker, domain):
		sport_duration = tracker.get_slot("sport_duration")
		sport_level = tracker.get_slot("sport_level")
		sport = tracker.get_slot("sport")
		period = tracker.get_slot("period")
		distance = tracker.get_slot("distance")
		response = """To sum up, you did some {} sport {} with a duration of {}.\nDEBUG : \n\tperiod : {}\n\tdistance : {}""".format(sport_level, sport, sport_duration, period, distance)
		dispatcher.utter_message(response)
		tracker.update(SlotSet("sport_duration",None))
		tracker.update(SlotSet("sport_level",None))
		tracker.update(SlotSet("sport",None))
