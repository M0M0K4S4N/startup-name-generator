import random
from .permutate import permutate
from .score import score
from .normalize import __normalize

# Names your shitty startup. Returns a list of possible names.
# @example
# 
#     namer('cloud')
#     namer('health fit')
#     namer(['health', 'fit'])
#     => ['Fitrise', 'Fityard', 'Healthup', ...]
# 

def namer(words, options={}):
    if isinstance(words, str):
        words = words.split(' ')
    word_list = permutate(words)
    # Random number generator
    gen = _get_random(options.get('seed', random.random()))
    rand = lambda: gen.uniform(0, 1)
    word_list = map(lambda word: {
        'word': __normalize(word),
        'score': score(word, rand)
    }, word_list)

    # Sort by score
    word_list = sorted(word_list, key=lambda word_score: -1 * word_score['score'])
    # Reduce to just words
    word_list = map(lambda word_score: word_score['word'], word_list)
    return list(word_list)

def _get_random(seed):
    return random.Random(seed)
