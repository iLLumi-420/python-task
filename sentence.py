sentence_list = [ 'This is first', 'This is second ', 'This is third', 'FOurth sentence', 'Also a sentence', 'Random word', 'Python is cool' ]

# def search(word):
#     for sentence in sentence_list:
#         if word in sentence:
#             return sentence
        

# print(search('Python'))

def create_index(sentence_list):
    index = {}
    for i, sentence in enumerate(sentence_list):
        words = sentence.split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(i)
    return index

index = create_index(sentence_list)
# print(index)

def search_word(word):
    if word not in index:
        return 'Not found'
    indices = index[word]
    return [sentence_list[i] for i in indices]

first_word = search_word('This')
second_word = search_word('Python')
third_word = search_word('adadda')

print(first_word, second_word, third_word)