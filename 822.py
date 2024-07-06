'''
Write a function to return true if the password is valid.
'''

def pass_validity(password):
    special_char = ['$', '@', '#', '%']
    if len(password) < 6:
        return False
    if len(password) > 16:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in special_char for char in password):
        return False
    return True


assert pass_validity("password")==False
assert pass_validity("Password@10")==True
assert pass_validity("password@10")==False
