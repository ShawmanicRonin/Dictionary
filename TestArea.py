# dic = {'bad':'don\'t', 'good':'do'}
# def search():
#     try:
#         word = str(input('What word do you want to define?\n\n\n>>'))
#         dicent = dic[word]
#         print(f'You\'r word is {str(dicent.capitalize)}\n\n\n\n\n')
#         search()
#     except:
#         print('Word not found\n\n\n\n\n')
#         search()

# search()

# def search_key_by_value(my_dict, value):
#     for key, val in my_dict.items():
#         if val == value:
#             return key
#     return None

# my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# value_to_search = 2
# result = search_key_by_value(my_dict, value_to_search)

# if result:
#     print(f"Key for value {value_to_search}: {result}")
# else:
#     print(f"Value {value_to_search} not found in the dictionary.")

# def search(my_dict):
#     key = input('>')
#     if key in my_dict:
#         print('I work', my_dict[key])
    
# search(my_dict)
# def fix():
#     KeyInput = input("What word would you like to define?\n\n\n>>")
#     while True:
#         try:
#             KeyInput = int(KeyInput)
#             print('I work.')
#             break
#         except:
#             print('I don\'t work')
#         fix()

# fix()

DictionaryVar = {"father" : "no, \"I\" am your father!", 'a':'I work'}
ErrorMessage = 'I don\'t work.'

# def Search():
#     InvalChars = ('0','1','2','3','4','5','6','7','8','9')
#     NoDef = f'No definition found.\n\nPerhapse the archives are incomplete?'
#     try:
#         KeyInput = input("What word would you like to define?\n\n\n>>")
#         if InvalChars in KeyInput:
#             print('I work')
#             #raise Exception('Please do not input intigers or floats.')
#         else:
#             Word = KeyInput.lower()
#             CapWord = Word.capitalize()
#             if Word.lower() == 'house':
#                 print('\n\n\n\n\nHouse\n\nThis is not for you.\n\n')
#             elif Word in DictionaryVar:
#                 DefVal = DictionaryVar.get(Word, NoDef)
#                 Def = DefVal.capitalize()
#                 print(f'\nThe definition of \"{CapWord}\" is...\n\n{Def}\n\n\n\n')
#             # elif KeyInput is not str:
#             #     raise Exception('Please do not input intigers or floats.')
#             #     Search()
#     except:
#         ErrorMessage
#     Search()
# Search()

def search():
    #def PrintInfo(KeyInput):

    InvalChars = ('0','1','2','3','4','5','6','7','8','9')
    InvalCharsStr = ''.join(InvalChars)
    NoDef = f'No definition found.\n\nPerhapse the archives are incomplete?'
    KeyInput = input("What word would you like to define?\n\n\n>>")
    Word = KeyInput.lower()
    CapWord = Word.capitalize()
    for i in KeyInput:
        if InvalCharsStr in KeyInput:
            print('I work')
            #raise TypeError(f'{KeyInput} is not accepted.')
        elif InvalCharsStr not in KeyInput:
            if Word.lower() == 'house':
                print('\n\n\n\n\nHouse\n\nThis is not for you.\n\n')
            elif Word in DictionaryVar:
                DefVal = DictionaryVar.get(Word, NoDef)
                Def = DefVal.capitalize()
                print(f'\nThe definition of \"{CapWord}\" is...\n\n{Def}\n\n\n\n')
    search()
search()