from itertools import permutations
 
def word_value(word, mapping):
    return int(''.join(str(mapping[ch]) for ch in word))
 
def solve(w1, w2, result):
    letters = sorted(set(w1 + w2 + result))
    leading = {w1[0], w2[0], result[0]}
    for digits in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, digits))
        if any(mapping[ch] == 0 for ch in leading):
            continue
        if word_value(w1, mapping) + word_value(w2, mapping) == word_value(result, mapping):
            return mapping
    return None
 
m = solve("SEND", "MORE", "MONEY")
print("Mapping:", m)
print("  ", word_value("SEND", m))
print("+ ", word_value("MORE", m))
print("= ", word_value("MONEY", m))
