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


def sortation(letters):
    sorted_list = []

    letters = return_characters()

    for stuff in letters:
        pass