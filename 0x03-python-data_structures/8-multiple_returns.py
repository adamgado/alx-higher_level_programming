#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        end_tuple = 0, "None"
    else:
        end_tuple = len(sentence), sentence[0]
    return end_tuple
