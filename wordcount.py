def word_count():
    with open("/Users/sreevedh/Bookbot/books/frankenstein.txt") as f:
        string = f.read()
    return string

def main():
    string  = word_count()
    count = string.split()
    message = (f"Found {len(count)} total words")
    return message

print(main())