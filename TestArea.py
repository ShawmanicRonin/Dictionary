dic = {'bad':'don\'t', 'good':'do'}
def search():
    try:
        word = str(input('What word do you want to define?\n\n\n>>'))
        dicent = dic[word]
        print(f'You\'r word is {str(dicent.capitalize)}\n\n\n\n\n')
        search()
    except:
        print('Word not found\n\n\n\n\n')
        search()

search()