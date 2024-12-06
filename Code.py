import sys
import webbrowser
import string
import random
ChoiceSeparator = '-' * 5
ErrorMessage = 'I don\'t work.'

DictionaryVar = {"house" : "this is not for you", "father" : "no, \"I\" am your father!"}

def Menu():
    print(f'\nWhat would you like to do?\n\n',
          'Search the Dictionary', ChoiceSeparator, '\b----- 1\n',
          'Retrieve a random entry', ChoiceSeparator, '\b--- 2\n',
          'Append the Dictionary', ChoiceSeparator, '\b----- 3\n',
          'Exit the Dictionary', ChoiceSeparator, '\b------- 4\n\n\n')
    MenuChoice = int(input('Please make a selection\n>>'))
    if MenuChoice == 1:
        Search()
    elif MenuChoice == 2:
        RandomWord()
    elif MenuChoice == 3:
        AppendDict()
    elif MenuChoice == 4:
        Exit()

def Search():
    try:
        Word = str.lower(input("What word would you like to define?\n\n\n>>"))
        DictionaryEntry = DictionaryVar.get(Word)
        if Word in DictionaryVar.keys:
            return DictionaryEntry.capitalize
    except:
        ErrorMessage

def RandomWord():
    try:
        RandomResult = random.choice(list(DictionaryVar.items))
        return RandomResult
    except:
        ErrorMessage

def AppendDict():
    try:
        NewWord = str(input('What word would you like to define?\n\n\n>>'))
        NewDef = str(input(f'What is the definition of {NewWord}?\n\n\n>>'))
        DictionaryVar.update({NewWord:NewDef})
        print(DictionaryVar)
    except:
        ErrorMessage


def Exit():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    sys.exit

Menu()