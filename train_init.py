from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import logging
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.augmented_memoization import AugmentedMemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	training_data_file = './data/stories.md'
	model_path = './models/dialogue'

	#fallback = FallbackPolicy(fallback_action_name="sum_up_fallback",core_threshold=0.3,nlu_threshold=0.3)
	
	featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(),
                                         max_history=5)
                                         
	#agent = Agent('domain.yml', policies = [AugmentedMemoizationPolicy(), KerasPolicy(featurizer), fallback])
	agent = Agent('domain.yml', policies = [AugmentedMemoizationPolicy(), KerasPolicy(featurizer)])

	agent.train(
			training_data_file,
			augmentation_factor = 50,
			epochs = 500,
			batch_size = 50,
			validation_split = 0.2)
			
	agent.persist(model_path)
