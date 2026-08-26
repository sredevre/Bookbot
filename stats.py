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

# This is the letter counting part of the assessment


def return_characters(string):
    letters = {}

    for char in string.lower():

        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

print(return_characters(get_book()))

# This is the sorting part of the assessment

def sort_on(letters: tuple[str, int]) -> int:
    return letters[1]


def chars_dict_to_sorted_list(letters):
    
    letters2 = letters:list[tuple[str, int]]
    return letters2

    letters = return_characters()

    for stuff in letters:
        pass
