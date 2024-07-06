'''
Write a python function to count number of vowels in the string.
'''

def Check_Vow(string, vowels):
    return len([each for each in string if each in vowels])


assert Check_Vow('corner','AaEeIiOoUu') == 2
assert Check_Vow('valid','AaEeIiOoUu') == 2
assert Check_Vow('true','AaEeIiOoUu') ==2
