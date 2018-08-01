#!/usr/bin/python
"""
This module is used to translate a RASA json file to another language.\n
Manually tag the entites later.\n
Created on Tue Jul 31 09:21:22 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
import sys
import json
import codecs
import requests
import getopt


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


def main(output, file_name, source, target, auth_key):
    to_save = translation(file_name, source, target, auth_key)
    if to_save is not None:
        # Save
        with open(output, 'w') as outfile:
            json.dump(to_save, outfile, ensure_ascii=False)

if __name__ == "__main__":
    available_languages = ["EN", "DE", "FR", "ES", "IT", "NL", "PL"]
    options, remainder = getopt.getopt(sys.argv[1:], 'o:f:s:t:k:h:', ['output=', 'file=', 'source=', 'target=', 'key=', 'help'])
    help_option = None    
    for opt, arg in options:
        if opt in ('-o', '--output'):
            output = arg
        elif opt in ('-f', '--file'):
            file_name = arg
        elif opt in ('-s', '--source'):
            source = arg
        elif opt in ('-t', '--target'):
            target = arg
        elif opt in ('-k', '--key'):
            auth_key = arg
        elif opt in ('-h', '--help'):
            help_option = True
    if help_option or len(sys.argv[1:]) != 10 or source not in available_languages or target not in available_languages:
        print("""usage: traduction.py\t[-h] -o OUTPUT_FILE_PATH -f INPUT_FILE_PATH
\t\t\t-s SOURCE_LANGUAGE -t TARGET_LANGUAGE
\t\t\t-k AUTH_KEY

example: traduction.py /home/ex/Desktop/MediBot/data/5_intents/risks/data.json\ FR EN df4385c2-33de-e423-4134-ca1f7b3ea8b7

translate a RASA json file to another language

arguments:
  -h, --help\t\toptional, show this help message and exit
  -o, --output\t\tlocation of the translated file
  -f, --file\t\tlocation of the file to translate
  -s, --source\t\tlanguage of the file to translate (among "EN", "DE", "FR", "ES", "IT", "NL", "PL")
  -t, --target\t\tlanguage of the file translated (among "EN", "DE", "FR", "ES", "IT", "NL", "PL")
  -k, --key\t\tauth key for DeepL API
        """)
    else:
        main(output, file_name, source, target, auth_key)
