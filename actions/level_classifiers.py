"""
This module is used to regroup classifier methods
Created on Tue Jun 26 10:22:40 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
from nltk.classify import PositiveNaiveBayesClassifier
from textblob import TextBlob
from ressources import get_examples_classif


def classifier(positive_featuresets, unlabeled_featuresets, text):
    """@param positive_featuresets: A list of featuresets
    that are known as positive examples (i.e., their label is ``True``).
    @param unlabeled_featuresets: A list of featuresets whose label is unknown.
    @param text: text to classify
    @return: The probability of the text to be classify positive\n
    A variant of the Naive Bayes Classifier that performs binary
    classification with
    partially-labeled training sets. In other words, assume we want to build
    a classifier that assigns each example to one of two complementary
    classes (e.g., male names and female names).\n
    If we have a training set with labeled examples for both classes,
    we can use a standard Naive Bayes Classifier. However, consider the case
    when we only have labeled examples for one of the classes, and other,
    unlabeled, examples.\n
    Then, assuming a prior distribution on the two labels, we can use the
    unlabeled set to estimate the frequencies of the various features.\n
    Let the two possible labels be 1 and 0, and let's say we only have
    examples labeled 1 and unlabeled examples. We are also given an estimate
    of P(1).\n
    We compute P(feature|1) exactly as in the standard case.\n
    To compute P(feature|0), we first estimate P(feature) from the unlabeled
    set (we are assuming that the unlabeled examples are drawn according to
    the given prior distribution)
    and then express the conditional probability as:\n
    P(feature|0) =(P(feature) - P(feature|1) * P(1))/P(0)"""
    classifier_naiv = PositiveNaiveBayesClassifier.train(positive_featuresets, unlabeled_featuresets)
    return classifier_naiv.prob_classify(features(text))


def features(sentence):
    """@param sentence: the sentence or word to check
    @return: a dictionnary of features"""
    words = sentence.lower().split()
    return dict(('contains(%s)' % w, True) for w in words)


def score(positive_words, text):
    """@param positive_words: a list of postives examples
    @param text: text to check
    @return: the number of time the text is in the positives examples"""
    raw_words = text.lower().split(" ")
    return len([word for word in raw_words if word in positive_words])


def get_level(text, language, level_to_find, possible_levels):
    """@param text: the word, corrected by C{TextBlob} to avoid mispelling
    @return: the level
    Call C{save_None} if None."""
    corrected = TextBlob(text).correct()
    [mild, moderate, severe] = get_examples_classif(level_to_find+"_level", possible_levels, language)
    not_mild = severe + moderate
    not_severe = mild + moderate
    not_moderate = severe + mild
    prob_sev = (classifier(list(map(features, severe)), list(map(features, not_severe)), corrected).prob(True))
    prob_mild = (classifier(list(map(features, mild)), list(map(features, not_mild)), corrected).prob(True))
    prob_mod = (classifier(list(map(features, moderate)), list(map(features, not_moderate)), corrected).prob(True))
#    print(prob_sev, prob_mild, prob_mod)
    best = max(prob_sev, prob_mild, prob_mod)
    if best <= 0.5:
        return save_none(corrected, text, level_to_find)
    if prob_mild == best:
        return possible_levels[0]
    elif prob_mod == best:
        return possible_levels[1]
    elif prob_sev == best:
        return possible_levels[2]
    else:
        return save_none(corrected, text, 'pain')


def get_physical_activity_level(text, language):
    """@param text: the sport's name
    @return: the sport's level 'little','moderate', 'vigorous' or None.
    Call C{save_None} if None."""
    return get_level(text, language, 'activity', ["vigorous", "moderate", "little"])


def get_pain_level(text, language):
    """@param text: the pain descritpion word
    @return: the pain level 'mild', 'moderate', 'severe' or None.
    Call C{save_None} if None."""
    return get_level(text, language, 'pain', ["mild", "moderate", "severe"])


def save_none(corrected, text, file_name):
    """@param corrected: corrected text
    @param text: text failed to be classified
    @param file_name: name of the file to save text
    @return: 'moderate' by default
    Save text and corrected in a file named file_name to allow them to
    be classified manually later."""
    file = open('./ressources/save_classif_'+file_name+'.txt', 'a+')
    file.write(str(corrected)+"\n"+str(text)+"\n")
    file.close()
    return 'moderate'
