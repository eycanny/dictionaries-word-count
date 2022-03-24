"""Count words in file."""
import sys


def tokenize(file_name):

    words = []

    with open(file_name) as input_file:
        for line in input_file:
            line = line.rstrip()
            word_list = line.split(" ")

            words.extend(word_list)

    return words


def count_words(words):
    """Take in a list of strings and return a dictionary of each string and the number 
    of times it appears in the list.
    
    """
    
    count_words = {}

    for word in words:
        count_words[word] = count_words.get(word,0) + 1

    return count_words
    

def print_word_counts(word_counts):
    for word in word_counts:
        print(word, word_counts[word])


def normalize_words(words):
    normalized_words = []

    for word in words:
        normalized_word = ""

        for char in word:
            if char.isalpha():
                normalized_word += char
        
        normalized_words.append(normalized_word.lower())

    return normalized_words


file = sys.argv[1]
tokens = tokenize(file)
normalized_words = normalize_words(tokens)
word_counts = count_words(normalized_words)
print_word_counts(word_counts)