#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    top_score = max(a_dictionary.values())
    for a in a_dictionary.items():
        if a_dictionary[a] == top_score:
            return a
