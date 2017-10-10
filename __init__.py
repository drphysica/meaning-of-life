from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger


__author__ = 'alex'

LOGGER = getLogger(__name__)


class MeaningOfLifeSkill(MycroftSkill):
    def __init__(self):
		super(MeaningOfLifeSkill, self).__init__(name="MeaningOfLifeSkill")

    def initialize(self):
		Meaning_Of_Life_Intent = IntentBuilder("MeaningOfLifeIntent").\
        	require("MeaningOfLifeKeyword").build()
    self.register_intent(Meaning_Of_Life_Intent, self.handle_MeaningOfLife_intent)

	
	def handle_MeaningOfLife_intent(self, message):
	    self.speak_dialog("MOL")    


    def stop(self):
		pass

def create_skill():
    return MeaningOfLifeSkill()
