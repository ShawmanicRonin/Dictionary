import sys
import webbrowser
import string
import random
ChoiceSeparator = '-' * 5
ErrorMessage = 'I don\'t work.'

DictionaryVar = {"father" : "no, \"I\" am your father!", 'a':'I work'}

def Menu():
    print(f'\nWhat would you like to do?\n\n',
          'Search the Dictionary', ChoiceSeparator, '\b----- 1\n',
          'Retrieve a random entry', ChoiceSeparator, '\b--- 2\n',
          'Append the Dictionary', ChoiceSeparator, '\b----- 3\n',
          'Exit the Dictionary', ChoiceSeparator, '\b------- 4\n\n\n')
    MenuChoice = int(input('Please make a selection.\n>>'))
    if MenuChoice == 1:
        Search()
    elif MenuChoice == 2:
        RandomWord(DictionaryVar)
    elif MenuChoice == 3:
        AppendDict(DictionaryVar)
    elif MenuChoice == 4:
        Exit()

def Search():
    InvalChars = ('0','1','2','3','4','5','6','7','8','9')
    try:
        NoDef = f'No definition found.\n\nPerhapse the archives are incomplete?'
        KeyInput = input("What word would you like to define?\n\n\n>>")
        KeyCheck = int(KeyInput)
        if KeyCheck is int is True:
            raise Exception('Please do not input intigers or floats.')
        else:
            Word = KeyInput.lower()
            CapWord = Word.capitalize()
            if Word.lower() == 'house':
                print('\n\n\n\n\nHouse\n\nThis is not for you.\n\n')
            elif Word in DictionaryVar:
                DefVal = DictionaryVar.get(Word, NoDef)
                Def = DefVal.capitalize()
                print(f'\nThe definition of \"{CapWord}\" is...\n\n{Def}\n\n\n\n')
            # elif KeyInput is not str:
            #     raise Exception('Please do not input intigers or floats.')
            #     Search()
    except:
        ErrorMessage
    Search()

def RandomWord(DictionaryVar):
    try:
        RandomResult = random.choice(list(DictionaryVar.items))
        return RandomResult
    except:
        ErrorMessage

def AppendDict(DictionaryVar):
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