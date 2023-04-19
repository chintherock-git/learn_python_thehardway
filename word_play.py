

def break_words(sentence):
    '''breaks words in sentence '''
    words=sentence.split(' ')
    return words

def first_word(words):
    '''gets first word in sentence'''
    words_list=words
    return words_list.pop(0)

def last_words(words):
    '''gets last word in sentence'''
    words_list=words
    return words_list.pop(-1)

def words_sorted(sentence):
    '''sorts words in sentence'''
    words_list=break_words(sentence)
    return sorted(words_list)

def sorted_first(sentence):
    '''gets first word on sorted sentence'''
    sort_list=words_sorted(sentence)
    return sort_list.pop(0)

def sorted_last(sentence):
    '''gets last word in sorted sentence'''
    sort_list=words_sorted(sentence)
    return sort_list.pop(-1)




