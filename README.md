# MediBot
A little chat bot

## Getting started 
* Install RASA doing :
```
sudo pip3 install -r requirements.txt
sudo python3 -m spacy download en
```

## Choose your pipeline
* For MITIE:
	* use this command to install MITIE backend (already in requirement.txt)
```
sudo pip3 install git+https://github.com/mit-nlp/MITIE.git
sudo pip3 install rasa_nlu[mitie]
```

	* now download MITIE Models
```
wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2
```

	* unzip the model
```
tar xvjf MITIE-models-v0.2.tar.bz2
```

	* we are interested in total_word_feature_extractor.dat file. This is inside MITIE-models/english folder. Move this file to /data folder
```
cp MITIE-models/english/total_word_feature_extractor.dat ./data/
rm MITIE-models-v0.2.tar.bz2
```

	* In the config.json file, add this where the word 'pipeline' is :
```
["nlp_mitie", "tokenizer_mitie", "ner_mitie", "ner_synonyms", "intent_entity_featurizer_regex", "intent_classifier_mitie"]
```

* For spacy_sklearn:
	* In the config.json file, add this where the word 'pipeline' is :
```
["nlp_spacy", "tokenizer_spacy", "intent_entity_featurizer_regex", "intent_featurizer_spacy", "ner_crf", "ner_synonyms",  "intent_classifier_sklearn"]
```

* For mitie_sklearn:
	* In the config.json file, add this where the word 'pipeline' is :
```
["nlp_mitie", "tokenizer_mitie", "ner_mitie", "ner_synonyms", "intent_entity_featurizer_regex", "intent_featurizer_mitie", "intent_classifier_sklearn"]
```

* To sum up:

template name | corresponding pipeline in config.json
------------ | -------------
spacy_sklearn | ["nlp_spacy", "tokenizer_spacy", "intent_entity_featurizer_regex", "intent_featurizer_spacy", "ner_crf", "ner_synonyms",  "intent_classifier_sklearn"]
mitie | ["nlp_mitie", "tokenizer_mitie", "ner_mitie", "ner_synonyms", "intent_entity_featurizer_regex", "intent_classifier_mitie"]
mitie_sklearn | ["nlp_mitie", "tokenizer_mitie", "ner_mitie", "ner_synonyms", "intent_entity_featurizer_regex", "intent_featurizer_mitie", "intent_classifier_sklearn"]

## Train NLU model
* _data.json_ file have to be filled with examples (text + entities in it + intent).
To do so :
	* manually complete json file
	* use rasa-nlu-trainer : `npm i -g rasa-nlu-trainer` and `rasa-nlu-trainer` in data folder
:heavy_exclamation_mark: Use Google Chrome!
* train the model with _data.json_ file :
```
python3 nlu_model.py
```

## Evaluate the model
To evaluate the model :
```
python3 -m rasa_nlu.evaluate -d data/data.json -m models/nlu/default/medibotnlu -c config.json
```
Or with cross validation :
```
python3 -m rasa_nlu.evaluate -d data/data.json -c config.json --mode crossvalidation
```

## Train bot
```
python3 train_init.py
```
To train 'online' (interactive learning) :

```
python3 train_online.py
```
Creates a file (stories.md by default). You have to add it into the stories.md file in /data

## Vizualize your stories
You can vizualize your stories by using graphviz. 
```
sudo apt-get install graphviz libgraphviz-dev graphviz-dev pkg-config
sudo pip3 install git+https://github.com/pygraphviz/pygraphviz
python3 vizualize.py
```

## Talk to bot :space_invader:

```
python3 dialogue_management_model.py
```
