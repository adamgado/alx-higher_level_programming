#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    b_score = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == b_score:
            return k
