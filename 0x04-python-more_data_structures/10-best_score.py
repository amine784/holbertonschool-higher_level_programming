#!/usr/bin/python3
def best_score(a_dictionary):
     if a_dictionary and len(a_dictionary):
        return(max(a_dictionary.keys()))
     if a_dictionary is None or a_dictionary == {}:
        return(None)
   
