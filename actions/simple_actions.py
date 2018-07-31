"""
This module is used to regroup all simple actions.\n
A simple action is an action where the bot just say something
or displays buttons\n
Created on Tue Jun 26 10:22:40 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button
from ressources import get_utterance


class AskAction(Action):
    """
    Used to say something to the user\n
    If self.SIMPLE is set, use its value for search utterance in ressources
    """
    SIMPLE = False
    entity_name = ""

    def check(self):
        """Used to check if all proprieties has been set"""
        if self.entity_name == "":
            raise NotImplementedError("""
            a AskAction action must implement a __init__ method
            with a entity_name""")

    def run(self, dispatcher, tracker, domain):
        """Print something for the user\n
        If self.SIMPLE is set, use its value for
        search utterance in ressources"""
        language = tracker.get_slot("language")
        if not self.SIMPLE:
            to_search_in_ressources = "ask_"+self.entity_name
        else:
            to_search_in_ressources = self.entity_name
        response = get_utterance(to_search_in_ressources, language)
        dispatcher.utter_message(response)

    def name(self):
        raise NotImplementedError("""a AskAction action must
                                    implement a name method""")


class AskBooleanAction(Action):
    """Used to say something to the user using two buttons (yes and no)\n
    If payload_no is set, a custom payload for 'No' will be used"""
    payload_no = None
    entity_name = ""
    intent_name = ""

    def check(self):
        """Used to check if all proprieties has been set"""
        if self.entity_name == "" or self.intent_name == "":
            raise NotImplementedError("""
            a AskAction action must implement a __init__ method
            with a entity_name AND a intent_name""")

    def run(self, dispatcher, tracker, domain):
        """Show two buttons (one for yes and one for no)\n
        If payload_no is set, a custom payload for 'No' will be used"""
        language = tracker.get_slot("language")
        message = get_utterance("ask_"+self.entity_name, language)
        yes_button = get_utterance("yes", language)
        no_button = get_utterance("no", language)
        buttons = []
        buttons.append(Button(title=yes_button,
                              payload="/"+self.intent_name+"{\""+self.entity_name+"\":true}"))
        if self.payload_no is None:
            buttons.append(Button(title=no_button,
                                  payload="/"+self.intent_name+"{\""+self.entity_name+"\":false}"))
        else:
            buttons.append(Button(title=no_button, payload=self.payload_no))
        dispatcher.utter_button_message(message, buttons)

    def name(self):
        raise NotImplementedError("""a AskBooleanAction action
                                    must implement a name method""")


class AskButtonsAction(Action):
    """Used to say something to the user using predefined buttons """
    entity_name = ""
    intent_name = ""
    buttons = []

    def check(self):
        """Used to check if all proprieties has been set"""
        if self.entity_name == "" or self.intent_name == "" or len(self.buttons) == 0:
            raise NotImplementedError("""
            a AskButtonsAction action must implement a __init__ method
            with a entity_name AND a intent_name AND a buttons list""")

    def run(self, dispatcher, tracker, domain):
        """For each button is self.buttons, make a
        button after the name button"""
        language = tracker.get_slot("language")
        message = get_utterance("ask_"+self.entity_name, language)
        buttons_to_show = []
        for button in self.buttons:
            name_button = get_utterance(button+"_button", language)
            buttons_to_show.append(Button(title=name_button,
                                          payload = "/" + self.intent_name + "{\"" + self.entity_name + "\":\"" + name_button.lower() + "\"}"))
        dispatcher.utter_button_message(message, buttons_to_show)

    def name(self):
        raise NotImplementedError("""a AskButtonsAction action
                                    must implement a name method""")


class AskMedicinal(AskBooleanAction):
    """Say something to the user : display buttons to tell
    if the treatment is medicinal or not
    When the "no" button is clicked, we have to set :
        - drug
        - dosing
        - treatment_being_taken
        - treatment_period
        - treatment_overdosage
    to something, saying that we won't ask
    anything about it for this treatment."""
    def __init__(self):
        """Set the name of the intent\n
        Set the name of the entity to ask"""
        self.entity_name = "medicinal"
        self.intent_name = "treatment"
        self.payload_no = "/treatment{\"medicinal\":false, \"drug\":\"no_drug\", \"dosing\":\"no_drug\", \"treatment_being_taken\":\"no_drug\", \"treatment_overdosage\":\"no_drug\"}"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_medicinal'


class AskActivityHard(AskBooleanAction):
    """Say something to the user :
    ask if the activity was hard to perform because of the general health"""
    def __init__(self):
        """Set the name of the intent\n
        Set the name of the entity to ask"""
        self.entity_name = "activity_hard"
        self.intent_name = "activity"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_activity_hard'


class AskSport(AskAction):
    """Say something to the user : ask the activity the user did"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "sport"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_sport'


class AskActivityDuration(AskAction):
    """Say something to the user : ask the duration of the activity"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "activity_duration"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_activity_duration'


class AskPainBodyPart(AskAction):
    """Say something to the user : ask the part of
    the body where the pain is"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pain_body_part"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain_body_part'


class AskPathologyBodyPart(AskAction):
    """Say something to the user : ask the body part where the pathology is"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pathology_body_part"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pathology_body_part'


class AskPainDuration(AskAction):
    """Say something to the user : ask the duration of the pain"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pain_duration"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain_duration'


class AskPainChange(AskButtonsAction):
    """Say something to the user :
    display buttons asking the evolution of the pain
    (brief, continuous, intermittent)"""
    def __init__(self):
        """Set the name of the entity to ask\n
        Set the name of the intent\n
        Set the list of available buttons to show to the user"""
        self.entity_name = "pain_change"
        self.intent_name = "pain"
        self.buttons = ["continuous", "intermittent", "brief"]

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain_change'


class AskPainPeriod(AskAction):
    """Say something to the user : ask the period of the pain"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pain_period"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain_period'


class AskActivityPeriod(AskAction):
    """Say something to the user : ask the period of the activity"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "activity_period"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_activity_period'


class AskActivity(AskAction):
    """Say something to the user :  ask the user to talk about his activity"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "activity"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_activity'


class AskSocial(AskAction):
    """Say something to the user :  ask the user to
    talk about his social activity"""
    def __init__(self):
        """ Set the name of the entity to ask"""
        self.entity_name = "social"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_social'


class AskHappiness(AskAction):
    """Say something to the user :  ask the user to talk about his happiness"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "happiness"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_emotionnal_hapiness'


class AskSadness(AskAction):
    """Say something to the user :  ask the user to talk about his sadness"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "sadness"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_emotionnal_sadness'


class AskPainDesc(AskAction):
    """Say something to the user :  ask the description of the pain"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pain_desc"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain_desc'


class AskSymptoms(AskAction):
    """Say something to the user : ask the symptoms"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "symtoms"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_symtoms'


class AskDrug(AskAction):
    """Say something to the user : ask the drug of the treatment
    We have to talk about that only if the treatment is medicinal"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "drug"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_drug'


class AskPainTime(AskAction):
    """Say something to the user : ask the begin date of the pain"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pain_time"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain_time'


class AskActivityTime(AskAction):
    """Say something to the user : ask the begin date of the activity"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "activity_time"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_activity_time'


class AskActivityDistance(AskAction):
    """Say something to the user : ask the distance of the activity"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "activity_distance"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_activity_distance'


class AskWeight(AskAction):
    """Say something to the user : ask the weight of the patient"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "weight"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_weight'


class AskInfoPatientDistance(AskAction):
    """Say something to the user : ask the size of the patients"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "infoPatient_distance"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_infoPatient_distance'


class AskHeartRate(AskAction):
    """Say something to the user : ask the heart rate of the patient"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "heart_rate"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_heart_rate'


class AskInfoPatientTemperature(AskAction):
    """Say something to the user : ask the temperature of the patient"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "infoPatient_temperature"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_infoPatient_temperature'


class AskGender(AskAction):
    """Say something to the user : ask the gender of the patient"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "gender"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_gender'


class AskBloodPressure(AskAction):
    """Say something to the user : ask the blood pressure of the patient"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "blood_pressure"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_blood_pressure'


class AskAddiction(AskAction):
    """Say something to the user : ask if the patient have an addicition"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "addiction"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_addiction'


class AskInfoPatientTime(AskAction):
    """Say something to the user : ask the last date of medical check up"""
    def __init__(self):
        """    Set the name of the entity to ask"""
        self.entity_name = "infoPatient_time"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_infoPatient_time'


class AskPathologyTime(AskAction):
    """Say something to the user : ask the begin
    time of pathology/side effect/symptom"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pathology_time"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pathology_time'


class AskPathologyPeriod(AskAction):
    """Say something to the user : ask the period
    of pathology/side effect/symptom"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pathology_period"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pathology_period'


class AskPathologyChange(AskBooleanAction):
    """Say something to the user :
    display buttons to tell if the pathology is worst or not"""
    def __init__(self):
        """Set the name of the intent\n
        Set the name of the entity to ask"""
        self.entity_name = "pathology_change"
        self.intent_name = "pathology"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pathology_change'


class AskPathologyTreatmentLinked(AskBooleanAction):
    """Say something to the user :
    display buttons to tell if the pathology is linked to the
    treatment or not (according to patient)"""
    def __init__(self):
        """Set the name of the intent\n
        Set the name of the entity to ask"""
        self.intent_name = "pathology"
        self.entity_name = "pathology_treatment_linked"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pathology_treatment_linked'


class AskDosing(AskAction):
    """Say something to the user : ask the dose the patient is taking
    (not the one prescripted)
    We have to talk about that only if the treatment is medicinal"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "dosing"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_dosing'


class AskTreatmentTime(AskAction):
    """Say something to the user : ask the begin date of the treatment taken"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "treatment_time"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_time'


class AskTreatmentBeingTaken(AskButtonsAction):
    """Say something to the user :
    display buttons to tell if the treatment is being well
    taken or forgotten or stopped
    When the "stopped" button is clicked, we have to set :
        - dosing
    to something, saying that we won't ask anything about
    it for this treatment."""
    def __init__(self):
        """Set the name of the entity to ask\n
        Set the name of the intent\n
        Set the list of available buttons to show to the user"""
        self.entity_name = "treatment_being_taken"
        self.intent_name = "treatment"
        self.buttons = ["taken", "stopped", "forgotten"]

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_being_taken'


class AskTreatmentOverdosage(AskButtonsAction):
    """Say something to the user :
    display buttons to tell if the treatment dose is well
    taken or overdose or under dose"""
    def __init__(self):
        """Set the name of the entity to ask\n
        Set the name of the intent\n
        Set the list of available buttons to show to the user"""
        self.entity_name = "treatment_overdosage"
        self.intent_name = "treatment"
        self.buttons = ["welltaken", "overdose", "underdose"]

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_overdosage'


class AskTreatmentPeriod(AskAction):
    """Say something to the user : ask the period of the medicinal treatment"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "treatment_period"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_period'


class AskTreatmentPrescripted(AskBooleanAction):
    """Say something to the user : display buttons to tell if
    the treatment is prescripted or not"""
    def __init__(self):
        """Set the name of the intent\n
        Set the name of the entity to ask"""
        self.intent_name = "treatment"
        self.entity_name = "treatment_prescripted"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_prescripted'


class AskTreatmentOk(AskBooleanAction):
    """Say something to the user :
    display buttons to tell if the patient feels ok about
    his treatment or not"""
    def __init__(self):
        """Set the name of the intent\n
        Set the name of the entity to ask"""
        self.intent_name = "treatment"
        self.entity_name = "treatment_ok"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_ok'


class AskRisk(AskAction):
    """Say something to the user : ask the user to talk about
    his risky behaviors"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "risk"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_risk'


class AskPain(AskAction):
    """Say something to the user : ask the user to talk about his pain"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "pain"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pain'


class Fallback(AskAction):
    """Say something to the user : fallback"""
    SIMPLE = True

    def __init__(self):
        """ Set the name of the entity to ask"""
        self.entity_name = "fallback"

    def name(self):
        """@return: the name of the action."""
        return 'sum_up_fallback'


class Agree(AskAction):
    """Say something to the user : tell that we understand the user agreed"""
    SIMPLE = True

    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "agree"

    def name(self):
        """@return: the name of the action."""
        return 'sum_up_agree'


class Disagree(AskAction):
    """Say something to the user : tell that we understand
    the user disagreed"""
    SIMPLE = True

    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "disagree"

    def name(self):
        """@return: the name of the action."""
        return 'sum_up_disagree'


class AskWhy(AskAction):
    """Say something to the user : asky why the user is sad"""
    def __init__(self):
        """ Set the name of the entity to ask"""
        self.entity_name = "why"

    def name(self):
        """@return: the name of the action."""
        return 'ask_why'


class Bye(AskAction):
    """Say something to the user : say bye"""
    SIMPLE = True

    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "bye"

    def name(self):
        """@return: the name of the action."""
        return 'sum_up_bye'


class Hello(AskAction):
    """Say something to the user : say hello"""
    SIMPLE = True

    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "hello"

    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_hello'


class AskTreatmentDuration(AskAction):
    """Say something to the user : ask the duration of the treatment"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "treatment_duration"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_treatment_duration'


class AskPathologyDuration(AskAction):
    """Say something to the user : ask the duration of the pathology"""
    def __init__(self):
        """Set the name of the entity to ask"""
        print("pathology_duration")
        self.entity_name = "pathology_duration"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_pathology_duration'


class AskSleep(AskAction):
    """Say something to the user : ask the user to talk about his sleep"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "sleep"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_sleep'


class AskEatingDisorders(AskAction):
    """Say something to the user : ask the user to talk about his
    eating disorder"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "eatingDisorders"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_eatingDisorders'


class AskDrugAddiction(AskAction):
    """Say something to the user : ask the user to talk about his
    drug addiction"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "drugAddiction"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_drugAddiction'


class AskSmoking(AskAction):
    """Say something to the user : ask the user to talk about his smoking"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "smoking"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_smoking'


class AskAlcohol(AskAction):
    """Say something to the user : ask the user to talk about his alcohol"""
    def __init__(self):
        """Set the name of the entity to ask"""
        self.entity_name = "alcohol"

    def name(self):
        """@return: the name of the action."""
        return 'utter_ask_alcohol'

# class AskNameOfEntity(AskAction):
#    """Say something to the user : ask"""
#    def __init__(self):
#        """Set the name of the entity to ask"""
#        print("pathology_duration")
#        self.entity_name = "nameOfEntity"
#
#    def name(self):
#        """@return: the name of the action."""
#        return 'utter_ask_nameOfEntity'

# class AskNameOfEntity(AskButtonsAction):
#    """Say something to the user :
#    display buttons to tell"""
#    def __init__(self):
#        """Set the name of the entity to ask\n
#        Set the name of the intent\n
#        Set the list of available buttons to show to the user"""
#        self.entity_name = "nameOfEntity"
#        self.intent_name = "nameOfIntent"
#        self.buttons = ["option1", "option2", "option3"]
#
#    def name(self):
#        """@return: the name of the action."""
#        return 'utter_ask_nameOfEntity'

# class AskNameOfEntity(AskBooleanAction):
#    """Say something to the user :
#    ask if"""
#    def __init__(self):
#        """Set the name of the intent\n
#        Set the name of the entity to ask"""
#        self.entity_name = "nameOfEntity"
#        self.intent_name = "nameOfIntent"
#
#    def name(self):
#        """@return: the name of the action."""
#        return 'utter_ask_nameOfEntity'
