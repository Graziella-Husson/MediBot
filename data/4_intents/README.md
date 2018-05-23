# 4 intents description
## 4 intents

* intent examples: 169 (4 distinct intents)
* Found intents: 'activity', 'pain_moderate', 'pain_severe', 'pain_mild'
* entity examples: 0 (0 distinct entities)
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 169 examples that have a defined intent out of 169 examples
	* F1-Score:  0.9881063592524821
	* Precision: 0.9884508861994791
	* Accuracy:  0.9881656804733728

## 4 intents + 4 entities

* intent examples: 343 (4 distinct intents)
* Found intents: 'emotional_sadness', 'activity', 'pain', 'emotional_hapiness'
* entity examples: 164 (4 distinct entities)
* found entities: 'pain_level', 'sport', 'body_part', 'duration'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 343 examples that have a defined intent out of 343 examples
	* F1-Score:  0.9941683077171756
	* Precision: 0.9943016167505964
	* Accuracy:  0.9941690962099126
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9318619144126725
	* Precision: 0.9323576213603415
	* Accuracy:  0.9347664936990363

## 4 intents + 7 entities

* intent examples: 345 (4 distinct intents)
* Found intents: 'emotional_sadness', 'pain', 'activity', 'emotional_hapiness'
* entity examples: 169 (6 distinct entities)
* found entities: 'body_part', 'duration', 'pain_level', 'distance', 'period', 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 345 examples that have a defined intent out of 345 examples
	* F1-Score:  0.99420211462896
	* Precision: 0.9943346508563901
	* Accuracy:  0.9942028985507246
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9351347397061957
	* Precision: 0.9394110662505769
	* Accuracy:  0.9392446633825944

## 4 intents + entities

* intent examples: 175 (4 distinct intents)
* Found intents: 'pain_severe', 'pain_mild', 'activity', 'pain_moderate'
* entity examples: 48 (1 distinct entities)
* found entities: 'sport'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 175 examples that have a defined intent out of 175 examples
	* F1-Score:  0.9885141412209685
	* Precision: 0.9888468558154969
	* Accuracy:  0.9885714285714285
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9778041767141582
	* Precision: 0.9782459928611454
	* Accuracy:  0.978433598183882







