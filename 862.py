'''
Write a function to find the occurrences of n most common words in a given text.
'''

def n_common_words(text, n):
    text = text.split()
    word_count = {}
    for word in text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return word_count[:n]


assert n_common_words("python is a programming language",1)==[('python', 1)]
assert n_common_words("python is a programming language",1)==[('python', 1)]
assert n_common_words("python is a programming language",5)==[('python', 1),('is', 1), ('a', 1), ('programming', 1), ('language', 1)]
