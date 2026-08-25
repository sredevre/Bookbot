## This the first part of the thing ##

def get_book():
    with open("/Users/sreevedh/Documents/Bookbot/Bookbot - Computing Project/books/frankenstein.txt") as f:
        string = f.read()
    return string

def main():
    string  = get_book()
    count = string.split()
    message = (f"Found {len(count)} total words")
    return message

print(main())

<<<<<<< HEAD
# This is the letter counting thing part of the assessment


def return_characters(string):
    letters = {}

    for char in string.lower():

        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

print(return_characters(get_book()))
=======
## This is the character counting thing part of the assessment ##

def return_characters(string):
    string.lower()
    
    
>>>>>>> 091c85642a56dd4c962eb59bc675fa32af0676da
