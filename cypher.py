#!/bin/bash
import sys



def cypher(sentence:str, n:int) -> str:
    #Uppercase letters 65-90
    #Lowercase letters 97-122
    sentence = sentence.upper()
    results = ""

    for letter in sentence:
        #Converts character to its numerical value
        new_letter = ord(letter)
        
        #Checks if characters numerical value is uppercase     
        if new_letter >= 65 and new_letter <=90:
            new_letter += int(n)
            if new_letter > 90:
                new_letter = abs(new_letter - 26)

        #Reverts character back from its numerical value 
        results += chr(new_letter)
        
    return results
n = sys.argv[1]
sentence = sys.argv[2]
print(cypher(sentence, n))
