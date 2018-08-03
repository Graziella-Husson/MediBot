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


def get_physical_activity_level(text, language):
    """@param text: the sport's name, corrected by C{TextBlob} to avoid mispelling
    @return: the sport's level 'little','moderate', 'vigorous' or None.
    Call C{save_None} if None."""
    corrected = TextBlob(text).correct()
    [vigorous, moderate, little] = get_examples_classif("physical_activity_level", ["vigorous", "moderate", "little"], language)
    not_little = vigorous + moderate
    not_vigorous = little + moderate
    not_moderate = vigorous + little
    prob_vig = (classifier(list(map(features, vigorous)), list(map(features, not_vigorous)), text).prob(True))
    prob_lit = (classifier(list(map(features, little)), list(map(features, not_little)), text).prob(True))
    prob_mod = (classifier(list(map(features, moderate)), list(map(features, not_moderate)), text).prob(True))
    print(prob_vig, prob_lit, prob_mod)
    best = max(prob_vig, prob_lit, prob_mod)
    if best <= 0.5:
        return save_none(corrected, text, 'save_classif_activity.txt')
    if prob_lit == best:
        return 'little'
    elif prob_mod == best:
        return 'moderate'
    elif prob_vig == best:
        return 'vigorous'
    else:
        return save_none(corrected, text, 'save_classif_activity.txt')


def get_pain_level(text, language):
    """@param text: the pain descritpion word, corrected by C{TextBlob}
    to avoid mispelling
    @return: the pain level 'mild', 'moderate', 'severe' or None.
    Call C{save_None} if None."""
    corrected = TextBlob(text).correct()
    [mild, moderate, severe] = get_examples_classif("pain_level", ["mild", "moderate", "severe"], language)
    not_mild = severe + moderate
    not_severe = mild + moderate
    not_moderate = severe + mild
    prob_sev = (classifier(list(map(features, severe)), list(map(features, not_severe)), corrected).prob(True))
    prob_mild = (classifier(list(map(features, mild)), list(map(features, not_mild)), corrected).prob(True))
    prob_mod = (classifier(list(map(features, moderate)), list(map(features, not_moderate)), corrected).prob(True))
    print(prob_sev, prob_mild, prob_mod)
    best = max(prob_sev, prob_mild, prob_mod)
    if best <= 0.5:
        return save_none(corrected, text, 'save_classif_pain.txt')
    if prob_mild == best:
        return 'mild'
    elif prob_mod == best:
        return 'moderate'
    elif prob_sev == best:
        return 'severe'
    else:
        return save_none(corrected, text, 'save_classif_pain.txt')


def save_none(corrected, text, file_name):
    """@param corrected: corrected text
    @param text: text failed to be classified
    @param file_name: name of the file to save text
    Save text and corrected in a file named file_name to allow them to
    be classified manually later."""
    file = open(file_name, 'a+')
    file.write(str(corrected)+"\n"+str(text)+"\n")
    file.close()
# if __name__ == '__main__':
#    text = TextBlob("sbrdeh")
#    res = get_pain_level(text)
#    print(res)
