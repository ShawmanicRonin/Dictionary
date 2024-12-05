class DictionaryClass:
    DictionaryVar = {"House" : "This is not for you", "Father" : "No, \"I\" am your father!"}

    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        DictionaryEntry = word + definition

    def Search():
        Word = str.lower(input("What word would you like to define?\n\n\n>>"))
        try:
            if Word in DictionaryClass.DictionaryVar.keys:
                return DictionaryClass.DictionaryVar[Word]
        except:
            print('I don\'t work')


    @classmethod
    def congragate_data(self, word, definition):
        pass
