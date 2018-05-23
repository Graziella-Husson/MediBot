from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot
from rasa_core.events import SlotSet

from rasa_core.events import (
    ActionExecuted,
    BotUttered,
    SlotSet,
    UserUttered
)
from rasa_core.actions.forms import (
    BooleanFormField,
    EntityFormField,
    FormAction,
    FreeTextFormField
)
from rasa_core.domain import TemplateDomain
from rasa_core.tracker_store import InMemoryTrackerStore
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.dispatcher import Dispatcher

class ActionSportDuration(Action):
	def name(self):
		return 'action_duration_sport'

	def run(self, dispatcher, tracker, domain):
		duration = tracker.get_slot("duration")
		tracker.update(SlotSet("sport_duration",duration))
		tracker.update(SlotSet("duration",None))

class ActionSportPeriod(Action):
	def name(self):
		return 'action_period_sport'

	def run(self, dispatcher, tracker, domain):
		duration = tracker.get_slot("period")
		tracker.update(SlotSet("sport_period",duration))
		tracker.update(SlotSet("period",None))

class ActionPainDuration(Action):
	def name(self):
		return 'action_duration_pain'

	def run(self, dispatcher, tracker, domain):
		duration = tracker.get_slot("duration")
		tracker.update(SlotSet("pain_duration",duration))
		tracker.update(SlotSet("duration",None))	

class ActionPainPeriod(Action):
	def name(self):
		return 'action_period_pain'

	def run(self, dispatcher, tracker, domain):
		duration = tracker.get_slot("period")
		tracker.update(SlotSet("pain_period",duration))
		tracker.update(SlotSet("period",None))	

class ActionFillSlotsSport(FormAction):
	RANDOMIZE = True

	@staticmethod
	def required_fields():
		return [
		EntityFormField("sport_duration", "sport_duration"),
		EntityFormField("sport", "sport")
		]

	def name(self):
		return 'action_check_slots_sport'

	def submit(self, dispatcher, tracker, domain):
		# TODO: get sport level
		tracker.update(SlotSet("sport_level","medium"))

		sport_duration = tracker.get_slot("sport_duration")
		sport_level = tracker.get_slot("sport_level")
		sport = tracker.get_slot("sport")
		period = tracker.get_slot("sport_period")
		distance = tracker.get_slot("distance")
		response = """To sum up, you did some {} sport: {} with a duration of {}""".format(sport_level, sport, sport_duration)
		
		if distance != None:
			response += """ and a distance of {}""".format(distance)
		if period != None:
			response +=""" and a period/recurrence of {}""".format(period)

		dispatcher.utter_message(response+".")
		return [SlotSet("sport_duration",None), SlotSet("sport_level",None), SlotSet("sport",None), SlotSet("distance",None), SlotSet("sport_period", None)]

class ActionFillSlotsPain(FormAction):
	RANDOMIZE = True

	@staticmethod
	def required_fields():
		return [
		EntityFormField("pain_duration", "pain_duration"),
		EntityFormField("pain_level", "pain_level"),
		EntityFormField("body_part", "body_part"),
		EntityFormField("pain_change","pain_change")
		]

	def name(self):
		return 'action_check_slots_pain'

	def submit(self, dispatcher, tracker, domain):
		pain_duration = tracker.get_slot("pain_duration")
		pain_level = tracker.get_slot("pain_level")
		body_part = tracker.get_slot("body_part")
		pain_change = tracker.get_slot("pain_change")
		period = tracker.get_slot("pain_period")
		response = """To sum up, you have some {} pain localized at {} with a duration of {}""".format(pain_level, body_part, pain_duration)
		if period != None:
			response += """ and a period/recurrence of {}""".format(period)
		response += """. The pain seems to be {}.""".format(pain_change)
		dispatcher.utter_message(response)
		return [SlotSet("pain_duration",None), SlotSet("pain_level",None), SlotSet("body_part",None), SlotSet("pain_change",None), SlotSet("pain_period",None)]
