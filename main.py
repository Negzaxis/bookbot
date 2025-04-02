"""Bookbot - to record # of words and characters"""
import sys
import requests
from stats import word_count
from stats import char_count
from stats import convert

# Check if there are exactly two arguments (script name + book path)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we get here, sys.argv[1] contains the book path
book_path = sys.argv[1]
# Now use book_path instead of a hardcoded path

def get_book_text():
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------""")
    file_contents = get_book_text()
    word_count(file_contents)
    char_count(file_contents)
    char_counts = char_count(file_contents)
    letter_dic = char_count(file_contents)
    sorted_characters = convert(letter_dic)
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")


if __name__ == "__main__":
    main()