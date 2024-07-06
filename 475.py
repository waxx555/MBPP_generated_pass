'''
Write a function to sort counter by value.
'''

def sort_counter(counter):
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)


assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
assert sort_counter({'Math':400, 'Physics':300, 'Chemistry':250})==[('Math', 400), ('Physics', 300), ('Chemistry', 250)]
assert sort_counter({'Math':900, 'Physics':1000, 'Chemistry':1250})==[('Chemistry', 1250), ('Physics', 1000), ('Math', 900)]
