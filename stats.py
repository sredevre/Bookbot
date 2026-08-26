## This the first part of the thing ##

def get_book():
    with open("/Users/sreevedh/Documents/Bookbot/Bookbot - Computing Project/books/frankenstein.txt") as f:
        string = f.read()
    return string


def main():
    string  = get_book()
    count = string.split()
    message = (f"Found {len(count)} total words")
    w_count = len(count)
    return message, w_count


# This is the letter counting part of the assessment


def return_characters(string):
    letters = {}

    for char in string.lower():

        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

# This is the sorting part of the assessment

def sort_on(letters: tuple[str, int]) -> int:
    return letters[1]


def chars_dict_to_sorted_list(letters: dict[str, int]):

    sorted_list = []

    for keys in letters:
        sorted_list.append((keys, letters[keys]))

    sorted_list = sorted(sorted_list, reverse=True, key=(sort_on))


    return sorted_list

print(chars_dict_to_sorted_list(return_characters(get_book())))