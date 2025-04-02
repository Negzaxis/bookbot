"""function for counting words"""

def word_count(file_contents):
    words = file_contents.split()
    num_of_words = len(words)
    print(f"Found {num_of_words} total words")


def char_count(file_contents):
    letters = file_contents.lower()
    letter_dic = {}
    for letter in letters:
        letter_dic[letter] = letter_dic.get(letter, 0) + 1
    return letter_dic

def sort_on(pair):
    return pair[1]  # The second element in the tuple (the count)

def convert(letter_dic):
    item_list = list(letter_dic.items())  # Convert items to a list of tuples
    item_list.sort(reverse=True, key=sort_on)  # Sort using the count (pair[1])
    return item_list