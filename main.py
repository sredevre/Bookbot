# Imports of stats.py functions and the sys function

import sys
from stats import return_characters, chars_dict_to_sorted_list, get_book

# This function creates the report

def print_report(path, w_count, sorted_list):

    #These are all the basic print calls for the start of the final report

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")

    #From here is the loop for the character count

    for alphabet in sorted_list:
        if alphabet[0].isalpha() == True:
            print(f"{alphabet[0]}: {alphabet[1]}")

    # Closing End line

    print("============= END ===============")


# This function brings in a lot of logic from stats.py in the Bookbot

def main():

    # sys.argv checks here

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # The rest of the normal function here

    path = sys.argv[1]
    string = get_book(sys.argv[1])
    count = string.split()
    w_count = len(count)
    sorted_list = chars_dict_to_sorted_list(return_characters(string))
    print_report(path, w_count, sorted_list)


# Calling the main() function

main()