# Unit Tests go here...
import pytest
from stats import return_characters, chars_dict_to_sorted_list, get_book


def test_get_book():
    # Tests that the path and its contents are read correctly
    result = get_book("test.txt")
    assert result == "Hello World!"


def test_return_characters():
    # Tests that letters are counted properly
    result = return_characters("hello")
    assert result["h"] == 1
    assert result["e"] == 1
    assert result["l"] == 2
    assert result["o"] == 1
   


def test_chars_dict_to_sorted_list():
    # Tests that the characters are sorted into a proper list
    result = chars_dict_to_sorted_list({
        "a": 3,
        "b": 1,
        "c": 2
    })

    assert result == [
        ("a", 3),
        ("c", 2),
        ("b", 1)
    ]
