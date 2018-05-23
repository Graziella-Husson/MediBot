# 6 intents description
## 6 intents + 7 entities

* intent examples: 515 (6 distinct intents)
* Found intents: 'emotional_sadness', 'fallback', 'activity', 'pain', 'emotional_hapiness', 'social'
* entity examples: 192 (6 distinct entities)
* found entities: 'sport', 'duration', 'body_part', 'period', 'distance', 'pain_level'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 515 examples that have a defined intent out of 515 examples
	* F1-Score:  0.9805711690228809
	* Precision: 0.9805822586429017
	* Accuracy:  0.9805825242718447
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9425985960699227
	* Precision: 0.9469840562884063
	* Accuracy:  0.946687573500588

## 6 intents + entities

* intent examples: 260 (6 distinct intents)
* Found intents: 'pain_severe', 'pain_moderate', 'activity', 'emotional_sadness', 'emotional_hapiness', 'pain_mild'
* entity examples: 48 (1 distinct entities)
* found entities: 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 260 examples that have a defined intent out of 260 examples
	* F1-Score:  0.9922691335141134
	* Precision: 0.9924930760296615
	* Accuracy:  0.9923076923076923
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9841536392212128
	* Precision: 0.9844550455995661
	* Accuracy:  0.9846625766871165

## 6 intents + entities + review examples

* intent examples: 234 (6 distinct intents)
* Found intents: 'emotional_hapiness', 'pain_mild', 'pain_moderate', 'emotional_sadness', 'pain_severe', 'activity'
* entity examples: 39 (1 distinct entities)
* found entities: 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 234 examples that have a defined intent out of 234 examples
	* F1-Score:  0.9700702156842508
	* Precision: 0.9707702207702208
	* Accuracy:  0.9700854700854701
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9884393548820234
	* Precision: 0.9884850862822332
	* Accuracy:  0.9887054735013032

## One word 6 intents + entity

* intent examples: 260 (6 distinct intents)
* Found intents: 'pain_severe', 'emotional_sadness', 'activity', 'pain_moderate', 'emotional_hapiness', 'pain_mild'
* entity examples: 43 (1 distinct entities)
* found entities: 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 260 examples that have a defined intent out of 260 examples
	* F1-Score:  0.9885078041588287
	* Precision: 0.9886404293381037
	* Accuracy:  0.9884615384615385
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9370687522891382
	* Precision: 0.9449791957167434
	* Accuracy:  0.9430255402750491







