# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:55:00 2018

@author: ex
"""
from duckling import DucklingWrapper
from ressources import get_language_duckling

language = 'ENG'
lang = get_language_duckling(language)
DUCKLING_WRAPPER = DucklingWrapper(language=lang)
print(DUCKLING_WRAPPER.parse('3 kilometers'))
