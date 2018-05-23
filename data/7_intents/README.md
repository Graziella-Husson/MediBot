# 7 intents description
## desambig 7 intents + entity

* intent examples: 309 (7 distinct intents)
* Found intents: 'emotional_hapiness', 'pain_mild', 'pain_moderate', 'activity', 'emotional_sadness', 'pain_severe', 'ambiguous_physical_emotionnal'
* entity examples: 48 (1 distinct entities)
* found entities: 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 309 examples that have a defined intent out of 309 examples
	* F1-Score:  0.977436978114332
	* Precision: 0.9781131279020685
	* Accuracy:  0.9773462783171522
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9843315858134295
	* Precision: 0.9848855831610196
	* Accuracy:  0.984993178717599

## fallback 7 intents + entity

* intent examples: 309 (7 distinct intents)
* Found intents: 'pain_mild', 'pain_moderate', 'fallback', 'emotional_hapiness', 'pain_severe', 'activity', 'emotional_sadness'
* entity examples: 48 (1 distinct entities)
* found entities: 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 309 examples that have a defined intent out of 309 examples
	* F1-Score:  0.9805089915922248
	* Precision: 0.9809358535403281
	* Accuracy:  0.9805825242718447
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.98560233640091
	* Precision: 0.9862025909307947
	* Accuracy:  0.9861717612809315




