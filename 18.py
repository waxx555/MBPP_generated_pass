'''
Write a function to remove characters from the first string which are present in the second string.
'''

def remove_dirty_chars(string1, string2):
    return ''.join([i for i in string1 if i not in string2])




assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles' 
