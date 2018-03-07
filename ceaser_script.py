#!/usr/bin/python
"""

I like Turtles
This is Caesar's Chipher
"""

import string

SHIFT = 3
HOICE = input("would you like to encode or decode?")
WORD = input("Please enter text")
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if CHOICE == "encode":
    for LETTER in WORD:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(LETTERS) + SHIFT
            ENCODED = ENCODED + LETTERS[x]
if CHOICE == "decode":
    for LETTER in WORD:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(LETTERS) - SHIFT
            ENCODED = ENCODED + LETTERS[x]
print(ENCODED)
