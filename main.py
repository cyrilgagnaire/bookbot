# main.py

# Imports
from stats import get_num_words, get_num_characters, sort_characters
import sys


# Function to read the content of a book from a file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


# Main function to execute the script
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    # word count
    words = get_num_words(get_book_text(filepath))
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    # stats
    print("--------- Character Count -------")

    letters = sort_characters(get_num_characters(get_book_text(filepath)))
    for letter in letters:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")

    # Footer
    print("============= END ===============")


# Entry point of the script
main()
