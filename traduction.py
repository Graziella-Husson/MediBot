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


def translation(file_name, source, target, auth_key):
    file = json.load(codecs.open(file_name, 'r', 'utf-8-sig'))
    to_save = file
    print("Translation...")
    ok = True
    for i in file['rasa_nlu_data']['common_examples']:
        for j in i:
            if j == 'text':
                r = requests.get('https://api.deepl.com/v1/translate?auth_key='+auth_key+'&text='+i[j]+'&source_lang='+source+'&target_lang='+target)
                try:               
                    trad = r.json()['translations'][0]['text']
                    replace_in_json(i[j], trad, to_save)
                except:
                    ok = False
                    print("Something bad happened with the API request, check your auth key and the paramaters")
    if ok:
        print("Done.")
        return to_save


def main(argv):
    available_languages = ["EN", "DE", "FR", "ES", "IT", "NL", "PL"]
    if len(argv) != 4 or argv[1] not in available_languages or argv[2] not in available_languages:
        print("Usage : python3 traduction.py FILE_PATH SOUCE_LANGUAGE TARGET_LANG AUTH_KEY")
        print("Example : python3 traduction.py /home/ex/Desktop/MediBot/data/5_intents/risks/data.json\ FR EN df4385c2-33de-e423-4134-ca1f7b3ea8b7")
    else:
        file_name = argv[0]
        source = argv[1]
        target = argv[2]
        auth_key = argv[3]
        to_save = translation(file_name, source, target, auth_key)
        if to_save is not None:
            # Save
            with open('data.json', 'w') as outfile:
                json.dump(to_save, outfile, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1:])
