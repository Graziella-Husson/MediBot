# MediBot :godmode:
A little chat bot

## Getting started :suspect:
* Install RASA doing:
```
sudo pip3 install -r requirements.txt
sudo python3 -m spacy download en_core_web_lg
sudo python3 -m spacy link en_core_web_lg en
sudo apt-get install python3-tk
```

To know wich version of RASA is currently installed:
```
sudo python3 -c "import rasa_nlu;import rasa_core;print(\"RASA NLU version: \"+rasa_nlu.__version__);print(\"RASA core version: \"+rasa_core.__version__)"
```

Or everything with:
```
sudo pip3 list
```
## Choose your pipeline :wrench:
You can follow these informations or directly use the .yml that you want in the config folder (e.g. config_spacy.yml for spacy pipeline).

* For MITIE:

Use this command to download MITIE Models

```
wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2
```


Unzip the model

```
tar xvjf MITIE-models-v0.2.tar.bz2
```

We are interested in total_word_feature_extractor.dat file. This is inside MITIE-models/english folder. Move this file to /data folder

```
cp MITIE-models/english/total_word_feature_extractor.dat ./data/
rm MITIE-models-v0.2.tar.bz2
```


In the conf.yml file, add this where the word 'pipeline' is:

```
pipeline:
- name: "nlp_mitie"
  model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_mitie"
- name: "ner_mitie"
- name: "ner_synonyms"
- name: "intent_entity_featurizer_regex"
- name: "intent_classifier_mitie"
```


* For spacy_sklearn:
	* In the conf.yml file, add this where the word 'pipeline' is:
```
pipeline:
- name: "nlp_spacy"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "ner_crf"
- name: "ner_synonyms"
- name: "intent_classifier_sklearn"
```

* For mitie_sklearn:
	* In the conf.yml file, add this where the word 'pipeline' is:
```
pipeline:
- name: "nlp_mitie"
  model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_mitie"
- name: "ner_mitie"
- name: "ner_synonyms"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_mitie"
- name: "intent_classifier_sklearn"
```

* For tensorflow_embedding:
	* In the conf.yml file, add this where the word 'pipeline' is:
```
pipeline:
- name: "intent_featurizer_count_vectors"
- name: "intent_classifier_tensorflow_embedding"
```

	* If you want to recognize many intents add intent_tokenization_flag and specify the split symbol:
```
  intent_tokenization_flag: true
  intent_split_symbol: "."
```
	

* Duckling for entity recognition: :baby_chick:
```
sudo apt-get install default-jdk
```

## Train NLU model :speech_balloon:
* _data.json_ file have to be filled with examples (text + entities in it + intent).
To do so:
	* manually complete json file
	* use rasa-nlu-trainer: `npm i -g rasa-nlu-trainer` and `rasa-nlu-trainer` in data folder
:heavy_exclamation_mark: Use Google Chrome!
* train the model with _data.json_ file:
```
python3 -m rasa_nlu.train -c config/conf.yml --fixed_model_name current --data data/data.json --path models/nlu
```

## Evaluate the model :hurtrealbad:
To evaluate the model:
```
python3 -m rasa_nlu.evaluate -d data/data.json -m models/nlu/default/current -c config/conf.yml
```
Or with cross validation (f=10 folds):
```
python3 -m rasa_nlu.evaluate -d data/data.json -c config/conf.yml --mode crossvalidation -f 10
```

## Train bot :books:
```
python3 train_init.py
```
To train 'online' (interactive learning):

```
python3 train_online.py
```

Creates a file (stories.md by default). You have to add it into the stories.md file in the data folder

### Vizualize your stories :eyes:

You can vizualize your stories by using graphviz. 
```
sudo apt-get install graphviz libgraphviz-dev graphviz-dev pkg-config
sudo pip3 install git+https://github.com/pygraphviz/pygraphviz
python3 vizualize.py
```

## Talk to bot :space_invader:

```
python3 -m rasa_core.run -d models/dialogue -u models/nlu/default/current
```

## Link your bot to a slack :electric_plug:
To link your bot to your slack you will need some tokens. You will find them in your api.slack.com app dashboard. Be sure to add a user bot and import the app into your workspace and a channel.
Add them in the file run_app.py then,

```
python3 run_app.py
```

Use ngrok to have the path to link into your api.slack.com app dashboard:

```
./ngrok http 5004
```

Then copy-paste the https URL in your api.slack.com app dashboard 'event-subscriptions' and add /webhook at the end.
When its saved, you will be able to talk to your bot in slack!

If your bot is using buttons, you will have to allow slack to use them. Go to the 'interactive component' part from dashboard on your api.slack.com app then add the https URL you took from ngrok and paste it in the request URL (allow interactive component first) and add /webhook at the end.
When its saved, you will be able to talk to your bot in slack with buttons!
