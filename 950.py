'''
Write a function to display sign of the chinese zodiac for given year.
'''

def chinese_zodiac(year):
    zodiac_signs = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep']
    return zodiac_signs[year % 12]


assert chinese_zodiac(1997)==('Ox')
assert chinese_zodiac(1998)==('Tiger')
assert chinese_zodiac(1994)==('Dog')
