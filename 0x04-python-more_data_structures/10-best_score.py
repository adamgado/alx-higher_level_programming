#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    score = 0
    for a in a_dictionary:
        if a_dictionary[a] > score:
            score = a_dictionary[a]
    return score
