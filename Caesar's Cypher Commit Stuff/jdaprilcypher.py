"""this is my Caesar's Cypher"""


import string

def encode(text):
    """this is my encoding function"""
    letters = string.ascii_letters + string.punctuation + string.digits + string.ascii_letters
    secret = ''
    for letter in text:
        if letter == ' ':
            secret = secret + ' '
        else:
            shifted = letters.index(letter) + 3
            secret = secret + letters[shifted]
    return secret

def decode(text):
    """this is my decode function"""
    letters = string.ascii_letters + string.punctuation + string.digits
    secret = ''
    for letter in text:
        if letter == ' ':
            secret = secret + ' '
        else:
            shifted = letters.index(letter) - 3
            secret = secret + letters[shifted]
    return secret

if __name__ == "__main__":
    ANSWER = input("would you like to encode or decode a word? ")
    TEXT = input("Please enter the text that you would like encoded/decode: ")
    if ANSWER == "encode":
        SECRET = encode(TEXT)
        print("Great, your new encoded word is", SECRET)
    elif ANSWER == "decode":
        SECRET = decode(TEXT)
        print("Awesome, your new decoded word is", SECRET)
    else:
        print("I'm sorry, I did not recognize your encode or decode command")

    print("Thank you for using our cypher")
