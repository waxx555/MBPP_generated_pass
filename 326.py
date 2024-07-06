'''
Write a function to get the word with most number of occurrences in the given strings list.
'''

def most_occurrences(strings):
    words = {}
    for string in strings:
        for word in string.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return max(words, key=words.get)


assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
assert most_occurrences(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
assert most_occurrences(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'
