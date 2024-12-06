import random
ErrorMessage = 'I don\'t work.'
class DictionaryClass:
    DictionaryVar = {"house" : "this is not for you", "father" : "no, \"I\" am your father!"}

    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        DictionaryEntry = word + definition

    def Search():
        try:
            Word = str.lower(input("What word would you like to define?\n\n\n>>"))
            DictionaryEntry = DictionaryClass.DictionaryVar.get(Word)
            if Word in DictionaryClass.DictionaryVar.keys:
                return DictionaryEntry.capitalize
        except:
            ErrorMessage

    def RandomWord():
        try:
            RandomResult = random.choice(list(DictionaryClass.DictionaryVar.items))
            return RandomResult
        except:
            ErrorMessage

    def AppendDict():
        try:
            NewWord = str(input('What word would you like to define?\n\n\n>>'))
            NewDef = str(input(f'What is the definition of {NewWord}?\n\n\n>>'))
            DictionaryClass.DictionaryVar.update({NewWord:NewDef})
            print(DictionaryClass.DictionaryVar)
        except:
            ErrorMessage

    @classmethod
    def congragate_data(self, word, definition):
        pass
