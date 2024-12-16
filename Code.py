import sys
import webbrowser
import string
import random
import time

#I was never able to get my program to work when importing the Dictionary from another file.
#from DictionaryHost import Dictionary
#import DictionaryHost

#used to make the menu code cleaner.
ChoiceSeparator = '-' * 5

#a general error message
ErrorMessage = 'I don\'t work.'

#Previous attempts to remap where the dictionary was pulled from
#DictionaryFile = Dictionary
#DictionaryVar = Dictionary

DictionaryVar = {"father" : "no, \"I\" am your father!", 'a':'I work'}
#TODO Create a start menu that branches to the other funcitons
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
        RandomWord()
    elif MenuChoice == 3:
        AppendDict()
    elif MenuChoice == 4:
        Exit()

#TODO Create a functoin that returns the desired entry
#I had an exceptionally difficult time getting digits excluded and understanding try except blocks.
def Search():
    NoDef = f'No definition found.\n\nPerhapse the archives are incomplete?'
    KeyInput = input("What word would you like to define?\n\n\n>>")
    translator = str.maketrans("", "", string.digits)
    Word = KeyInput.translate(translator)
    try:
        if Word == '':
            print('Please do not input intigers or floats.')
        elif Word == '.':
            print('Please do not input intigers or floats.')
        else:
            Word = KeyInput.lower()
            CapWord = Word.capitalize()
    except Exception:
        print('Please don\'t confuse me.')
    else:
        if Word.lower() == 'house':
                print('\n\n\n\n\nHouse\n\nThis is not for you.\n\n')
        elif Word in DictionaryVar:
                DefVal = DictionaryVar.get(Word, NoDef)
                Def = DefVal.capitalize()
                print(f'\nThe definition of \"{CapWord}\" is...\n\n{Def}\n\n\n\n')
        else:
            print(f'{Word.capitalize()} is not in the dictionary.\n{NoDef}')
    finally:
        time.sleep(5)
        NextFunction()

#TODO create a function that returns a random entry.
def RandomWord():
    try:
        DictionaryLst = list(DictionaryVar.items())
        key, value = random.choice(DictionaryLst)
    except:
        print(ErrorMessage)
    else:
        print(f'\n The definition of \"{key} is...\n\n{value}\n\n\n\n')
    finally:
        time.sleep(5)
        NextFunction()

#TODO create a function that allows the user to edit the dictionary contents
def AppendDict():
    translator = str.maketrans("", "", string.digits)
    try:
        NewWordInput = str(input('What word would you like to define?\n\n\n>>'))
        NewWordLower = NewWordInput.lower()
        NewWord = NewWordLower.translate(translator)
        if NewWord == '':
            print('Please do not input intigers or floats.')
        elif NewWord == '.':
            print('Please do not input intigers or floats.')
        else:
            NewDefInput = str(input(f'What is the definition of {NewWord}?\n\n\n>>'))
            NewDefLower = NewDefInput.lower()
            NewDef = NewDefLower.translate(translator)
            DictionaryVar.update({NewWord:NewDef})
            print(DictionaryVar)
    except:
        print(ErrorMessage)
    finally:
        time.sleep(5)
        NextFunction()

#This function was intended to save the latest verson of the dictionary
# def SaveEdits(DictionaryVar, DictionaryHost):
#     with open(DictionaryHost, 'w') as f:
#         f.write(DictionaryVar)

#Recent research on reading an iterated file
# def ReadLog(DictionaryHost):
#     with open(DictionaryHost, 'r') as f:
#         read = f.read()
#         return read

#TODO create a function that closes the program
def Exit():
    #I wanted to save just before the program closed
    #SaveEdits(DictionaryVar, DictionaryHost)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    sys.exit

def NextFunction():
    print(f'\nWhat would you like to do next?\n\n',
          'Search the Dictionary', ChoiceSeparator, '\b----- 1\n',
          'Retrieve a random entry', ChoiceSeparator, '\b--- 2\n',
          'Append the Dictionary', ChoiceSeparator, '\b----- 3\n',
          'Exit the Dictionary', ChoiceSeparator, '\b------- 4\n\n\n')
    MenuChoice = int(input('Please make a selection.\n>>'))
    if MenuChoice == 1:
        Search()
    elif MenuChoice == 2:
        RandomWord()
    elif MenuChoice == 3:
        AppendDict()
    elif MenuChoice == 4:
        Exit()