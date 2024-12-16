DictionaryVar = {"father" : "no, \"I\" am your father!", 'a':'I work'}
import random
# dictionary = {"father" : "no, \"I\" am your father!", 'a':'I work'}

# def search_dict(dictionary, search_string):
#     if not search_string.isalpha():
#         raise ValueError("Search string should not contain number characters.")
#         return {k: v for k, v in dictionary.items() if search_string in k}
  
# def randkey():
#     DictionaryLst = list(DictionaryVar.items())
#     rand = random.choice(DictionaryLst)
#     print(rand)
# randkey()

def randkey():
    DictionaryLst = list(DictionaryVar.items())
    key, value = random.choice(DictionaryLst)
    print(f'The definition of {key} is {value}')
randkey()