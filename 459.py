'''
Write a function to remove uppercase substrings from a given string by using regex.
'''

import re

def remove_uppercase(s):
    return re.sub(r'[A-Z]', '', s)


assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
