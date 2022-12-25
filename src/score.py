from .utils import syllable_count
from .normalize import __normalize
from .constants import ACTUAL_SUFFIXES

# Scores a word
# 
# @param {Function} rand Random number generator
# 
def score(word, rand):
    score = 0
    score += __score_syllables(word)
    score += __score_suffix(word)
    score += __score_length(word)
    score += rand() * 0.4
    return score


# Scores a word based on syllables
def __score_syllables(word):
    syllables = syllable_count(word)
    if syllables == 2:
        return 6.1
    elif syllables == 3:
        return 6
    elif syllables > 4:
        return 2
    else:
        return 4


# Scores a word based on suffixes
def __score_suffix(word):
    is_actual = any([word[-len(suffix):] == suffix for suffix in ACTUAL_SUFFIXES])
    if is_actual:
        return -1.5
    else:
        return 0

# Scores a word based on length
def __score_length(word):
    try:
        length = len(__normalize(word))
    except TypeError:
        return 0

    if length < 9:
        return 0.1
    else:
        return 0
