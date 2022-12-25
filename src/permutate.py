from .constants import PREFIXES, SUFFIXES

# /*
#  * Adds suffixes and prefixes to words
#  */

def permutate(words: list):
    if len(words) == 0:
        return permutate_fixes(PREFIXES, SUFFIXES)
    else:
        return permutate_fixes(PREFIXES, words) \
            + permutate_fixes(words, SUFFIXES)

# /*
#  * I'm feeling lucky
#  */

def permutate_fixes(prefixes: list, suffixes: list):
    return [ \
        f"{prefix} {suffix}" \
            for prefix in prefixes \
                for suffix in suffixes \
                    if prefix != suffix
    ]
