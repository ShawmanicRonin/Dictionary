import sys
import webbrowser
import string
from Dictionary import DictionaryClass
choice_separator = '-' * 5

def Menu():
    print(f'\nWhat would you like to do?\n\n',
          'Search the Dictionary', choice_separator, '\b----- 1\n',
          'Retrieve a random entry', choice_separator, '\b--- 2\n',
          'Append the Dictionary', choice_separator, '\b----- 3\n',
          'Exit the Dictionary', choice_separator, '\b------- 4')
    menu_choice = int(input('>'))
    if menu_choice == 1:
        search()
    elif menu_choice == 2:
        random_word()
    elif menu_choice == 3:
        append()
    elif menu_choice == 4:
        exit()

def search():
    search_input = (str(input(f'\nWhat word would you like to define?\n\n\n>')))
    try:
        if search_input in DictionaryClass.DictionaryVar.keys:
            print('I work')
    except:
        print('I dont work')

def random_word():
    pass

def append():
    pass

def exit():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    sys.exit

Menu()