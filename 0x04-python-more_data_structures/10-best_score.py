#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    score = max(a_dictionary)
    for a in a_dictionary:
        if a_dictionary[a] == score:
            return a
