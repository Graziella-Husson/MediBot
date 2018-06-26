# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

def run_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('../models/nlu/default/current')
	agent = Agent.load('../models/dialogue/actionsOK', interpreter = interpreter)
	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())
	return agent
	
if __name__ == '__main__':
	agent = run_bot()
