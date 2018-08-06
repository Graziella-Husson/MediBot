"""
This module is used to regroup functions related to ressources
Created on Tue Jun 26 10:22:40 2018\n
Last update on Mon Jul 30 10:30:00 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
import json
import csv
from duckling.language import Language


def get_utterance(key, language):
    """@param key: id of the sentence to search for in ressources.json file
    @param language: language to use
    @return: the utterance the bot have to say for a given key and language"""
    ressources = json.load(open('ressources.json'))
    utterance = ressources['utterances'][key][language]
    return utterance


def get_language_duckling(language):
    """@param language: language to use
    @return: the language to use with Duckling"""
    return {
        'FRA': Language.FRENCH,
        'ENG': Language.ENGLISH
        }.get(language, None)


def get_examples_classif(level_type, keys, language):
    """@param level_type: ID of the type of leve e.g. pain_level.
    @param keys: list of ids of the examples to search for in ressources.json
    file e.g. ['vigorous', 'moderate', 'little']
    @param language: language to use
    @return: list of examples for each keys"""
    ressources = json.load(open('ressources.json'))
    examples_classif = []
    for key in keys:
        examples_classif.append(ressources['examples_classif'][level_type][key][language])
    return examples_classif


#def get_drug_info(drug):
#    to_return = []
#    with open('/home/ex/Desktop/MediBot/actions/FDA_druglist_2018.csv', 'r') as csvfile:
#        spamreader = csv.reader(csvfile, delimiter=';')
#        for row in spamreader:
#            # [prod_id, prod_ndc, name, propriety_name, proprietu_name_suffix,
#            # non_propriety_name, dosage_form_name, route_name,
#            # start_marketing_date, end_marketing_date,
#            # marketing_category_name, app_number, labeler_name, subst_name,
#            # active_numerator_strength, active_ingred_unit, pharm_classes,
#            # deaschedule, ndc_exclude_flag, listing_record_certified] = row
#            if drug in row:
#                to_return.append(row)
#    return to_return

            
#print(get_drug_info("LULICONAZOLE"))