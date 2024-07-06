'''
Write a function to perform the concatenation of two string tuples.
'''

def concatenate_strings(t1, t2):
    return tuple([i + j for i, j in zip(t1, t2)])


assert concatenate_strings(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
assert concatenate_strings(("Shaik", "Ayesha", "Sanya"), (" Dawood", " Begum", " Singh")) == ('Shaik Dawood', 'Ayesha Begum', 'Sanya Singh')
assert concatenate_strings(("Harpreet", "Priyanka", "Muskan"), ("Kour", " Agarwal", "Sethi")) == ('HarpreetKour', 'Priyanka Agarwal', 'MuskanSethi')
