# stats.py


# A simple function to count the number of words in a given text
def get_num_words(text):
    return len(text.split())


# A function that takes a string and returns the number of times each character, (including symbols and spaces), appears in the string.
def get_num_characters(text):
    char_count = {}
    for char in text:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count


# A function that takes a dictionary and returns the value of the "num" key
def sort_on(items):
    return items["num"]


# A function that takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
def sort_characters(char_dict):
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    return sorted(char_list, key=sort_on, reverse=True)
