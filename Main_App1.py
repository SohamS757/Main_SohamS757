import json
import difflib
from difflib import get_close_matches
word = input('Enter the Word: ')

data = json.load(open('data.json'))

def Asking_Question(word):
    user_input = input(f'Enter Y if you meant {get_close_matches(word,data.keys())[0]} or N for No: ')
    if user_input == 'Y':
        return data[get_close_matches(word,data.keys())[0]]
    elif user_input == 'N':
        return 'Please Double Check The Word You Entered'
    else:
        return "We Couldn't understand your word"

def transalation(word):
    if isinstance(word,str):
        if word in data.keys():
            word = data[word]
            return word
        elif word not in data:
            word_list = [word.upper(),word.lower(),word.capitalize(),word.title()]
            for mainwrd in word_list:
                if mainwrd in data.keys():
                    word = mainwrd
                    return data[word]
            if len(get_close_matches(word,data.keys())) > 0:
                return Asking_Question(word)
            else:
                return 'Invalid Input'
        else:
            return 'Invalid Input'

main_output = transalation(word)
if isinstance(main_output,list):
    for main_word in main_output:
        print(main_word)
else:
    print(main_output)