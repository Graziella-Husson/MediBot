#!/usr/bin/python

"""
Created on Tue Jul 31 09:21:22 2018

@author: ex
"""
import sys
import json
import codecs
import requests


def replace_in_json(old, new, to_save):
    for i in to_save['rasa_nlu_data']['common_examples']:
        for j in i:
            if j == 'text' and i[j] == old:
                i[j] = new


def translation(file_name, source, target):
    file = json.load(codecs.open(file_name, 'r', 'utf-8-sig'))
    to_save = file
    print("Translation...")
    for i in file['rasa_nlu_data']['common_examples']:
        for j in i:
            if j == 'text':
                r = requests.get('https://api.deepl.com/v1/translate?auth_key=9fdd7cc8-8c5e-dd47-1f6a-7d3b8612221e&text='+i[j]+'&source_lang='+source+'&target_lang='+target)
                trad = r.json()['translations'][0]['text']
                replace_in_json(i[j], trad, to_save)
    print("Done.")
    return to_save


def main(argv):
    available_languages = ["EN", "DE", "FR", "ES", "IT", "NL", "PL"]
    if len(argv) != 3 or argv[1] not in available_languages or argv[2] not in available_languages:
        print("Usage : python3 traduction.py FILE_PATH SOUCE_LANGUAGE TARGET_LANG")
        print("Example : python3 traduction.py /home/ex/Desktop/MediBot/data/5_intents/risks/data.json\ FR EN")
    else:
        file_name = argv[0]
        source = argv[1]
        target = argv[2]
        to_save = translation(file_name, source, target)
        # Save
        with open('data.json', 'w') as outfile:
            json.dump(to_save, outfile, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1:])
