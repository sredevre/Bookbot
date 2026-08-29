# This the first part of the assessment which opens the book itself

def get_book(path):
    with open(path) as f:
        string = f.read()

    return string


# This is the letter counting part of the assessment

# This function counts the letters and puts them into a dictionary

def return_characters(string):
    letters = {}

    for char in string.lower():

        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters


# This is the sorting part of the assessment

# Definition of the sort on function to be used for the next function

def sort_on(letters: tuple[str, int]) -> int:
    return letters[1]


# This function is used to make the neat clean list by cleaning the messy dictionary

def chars_dict_to_sorted_list(letters: dict[str, int]):

    sorted_list = []

    for keys in letters:
        sorted_list.append((keys, letters[keys]))

    sorted_list = sorted(sorted_list, reverse=True, key=(sort_on))


    return sorted_list
