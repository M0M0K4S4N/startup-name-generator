import re

# Normalizes a word.
# @private
# @example
# 
#     normalize('cloud layer')
#     => 'Cloudlayer'
# 
#     normalize('time ible')
#     => 'Timible'
# 
def __normalize(word: str):
    w = word \
        .replace(r'e i', 'i') \
        .replace(r'th t', 't')

    w = re.sub(r'(.) (.)', lambda m: m.group(1) if m.group(1) == m.group(2) else m.group(1) + m.group(2), w)
    w = w.title()

    return w
