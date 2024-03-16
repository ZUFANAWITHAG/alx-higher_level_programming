#!/usr/bin/python3
def multiple_returns(sentence):
    myTupl = ()
    if len(sentence) == 0:
        myTupl = 0, "None"
    else:
        myTupl = len(sentence), sentence[0]
