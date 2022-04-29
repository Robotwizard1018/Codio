#!/bin/bash
import sys

def cipher(sentence:str, n:int) -> str:
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
            results += chr(new_letter)

        #Reverts character back from its numerical value 
        # results += chr(new_letter)
        
    return results

n = sys.argv[1]
charcount = 0
linecount = 0
output = ""

for line in sys.stdin:
  #Encodes each line by the desired ammount
  line = cipher(line, n)

  for char in line:
    charcount += 1
    output += char

    #Adds a space every five characters
    if charcount % 5 == 0:
      output += " "
      linecount += 1

    #Adds a new line every ten blocks of five characters
    if linecount == 10:
      output += "\n"
      linecount = 0

print(output)




    
    
  
