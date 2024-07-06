'''
Write a function to remove everything except alphanumeric characters from a string.
'''

def remove_splchar(s):
    return ''.join(i for i in s if i.isalnum())


assert remove_splchar('python  @#&^%$*program123')==('pythonprogram123')
assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')
assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program')==('python67program')
