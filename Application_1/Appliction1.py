# Comparing the dictionary key and the user word value using the difflib

import difflib
import json

# load json data in the data variable

data = json.load(open("data.json"))

# Define the function that find the word in data dictionary

def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(difflib.get_close_matches(w,data.keys()))>0:
        responce =  input(f"Did you mean {difflib.get_close_matches(w,data.keys())[0]}? y or n : ").lower()
        if responce == "y" or responce=="yes":
            return data[difflib.get_close_matches(w,data.keys())[0]]
        elif responce =="n" or responce=="no":
            return "The word not exists. pleases double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word not exists. pleases double check it. "


# Take User Input

word = input("Enter Word: ").lower()

# Store The Output

output =translate(word)

# Printing The Output

if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)