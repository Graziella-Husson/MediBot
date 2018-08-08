"""
This module is used to regroup functions related to ressources
Created on Tue Jun 26 10:22:40 2018\n
Last update on Mon Jul 30 10:30:00 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
import json
import csv
from duckling.language import Language
from insertfonction import insert_to_conversation


def get_utterance(key, language):
    """@param key: id of the sentence to search for in ressources.json file
    @param language: language to use
    @return: the utterance the bot have to say for a given key and language"""
    ressources = json.load(open('./ressources/ressources.json'))
    utterance = ressources['utterances'][key][language]
    insert_to_conversation(utterance,"BOT")
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
    ressources = json.load(open('./ressources/ressources.json'))
    examples_classif = []
    for key in keys:
        examples_classif.append(ressources['examples_classif'][level_type][key][language])
    return examples_classif


def get_drug_info(drug, language):
    """@param drug: drug name or marketing name of the drug
    @return: call C{clean_info_drug} method with list of drug found in file
    [propriety_name, non_propriety_name, subst_name, pharm_classes]
    """
    to_return = []
    with open('./ressources/FDA_druglist_2018.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            # [prod_id, prod_ndc, type, propriety_name, propriety_name_suffix,
            # non_propriety_name, dosage_form_name, route_name,
            # start_marketing_date, end_marketing_date,
            # marketing_category_name, app_number, labeler_name, subst_name,
            # active_numerator_strength, active_ingred_unit, pharm_classes,
            # deaschedule, ndc_exclude_flag, listing_record_certified] = row
            if drug in [x.lower() for x in row]:
                infos = [row[3], row[5], row[13], row[16]]
                to_return.append(infos)
    return clean_info_drug(to_return, drug, language)


def clean_info_drug(list_infos, drug, language):
    """@param list_infos: list of infos for several drugs with a name in common
    @return: [propriety_names, non_propriety_names, subst_names, pharm_classes]
    if drug is not found in file, returns ['drug (default value)',
    'drug (default value)', 'drug (default value)', 'drug (default value)']
    """
    propriety_names = ""
    non_propriety_names = ""
    subst_names = ""
    pharm_classes = ""
    for info in list_infos:
        if info[0] not in propriety_names:
            propriety_names += "/" + info[0]
        if info[1] not in non_propriety_names:
            non_propriety_names += "/" + info[1]
        if info[2] not in subst_names:
            subst_names += "/" + info[2]
        if info[3] not in pharm_classes:
            pharm_classes += "/" + info[3]
    infos = [propriety_names, non_propriety_names, subst_names, pharm_classes]
    count = 0
    for inf in infos:
        if inf == "":
            infos[count] = drug.title() + get_utterance("default", language)
        else:
            infos[count] = inf.title()[1:]
        count += 1
    return infos
