import string

def encode(text):
    letters = string.ascii_letters + string.punctuation + string.digits
    secret = ''
    for letter in text:
        if letter == ' ':
            secret = secret + ' '
        else:
            shifted = letters.index(letter) + 3
            secret = secret + letters[shifted]
    return secret
        
def decode(text):
    letters = string.ascii_letters + string.punctuation + string.digits
    secret = ''
    for letter in text:
        if letter == ' ':
            secret = secret + ' '
        else:
            shifted = letters.index(letter) - 3
            secret  = secret + letters[shifted]
    return secret

if __name__ == "__main__":
    answer = input("would you like to encode or decode a word? ")
    text = input("Please enter the text that you would like encoded/decode: ")
    if answer == "encode":
        secret = encode(text)
        print("Great, your new encoded word is",secret)
    elif answer == "decode":
        secret = decode(text)
        print("Awesome, your new decoded word is", secret)
    else:
        print("I'm sorry, I did not recognize your encode or decode command")
    
    print("Thank you for using our cypher")


