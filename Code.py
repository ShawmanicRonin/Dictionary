import sys
import webbrowser
import string
from Dictionary import DictionaryClass
ChoiceSeparator = '-' * 5

def Menu():
    print(f'\nWhat would you like to do?\n\n',
          'Search the Dictionary', ChoiceSeparator, '\b----- 1\n',
          'Retrieve a random entry', ChoiceSeparator, '\b--- 2\n',
          'Append the Dictionary', ChoiceSeparator, '\b----- 3\n',
          'Exit the Dictionary', ChoiceSeparator, '\b------- 4\n\n\n')
    MenuChoice = int(input('>>'))
    if MenuChoice == 1:
        DictionaryClass.Search()
    elif MenuChoice == 2:
        RandomWord()
    elif MenuChoice == 3:
        Append()
    elif MenuChoice == 4:
        Exit()

def RandomWord():
    pass

def Append():
    pass

def Exit():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    sys.exit

Menu()