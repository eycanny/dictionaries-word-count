"""Count words in file."""
import sys

input_file = open(sys.argv[1])


def tokenize(file_name=input_file):

    words = []  
    for line in file_name:
        line = line.rstrip()
        word_list = line.split(" ")

        for word in word_list:
            if word not in words:
                words.append(word)

    return words

def count_words(words):
    """Take in a list of strings and return a dictionary of each string and the number 
    of times it appears in the list.
    
    """
    
    count_words = {}

    for word in words:
        count_words[word] = count_words.get(word,0) + 1

    return count_words
    
# input_file.close()

# for word in word_counts:
#     print(word, word_counts[word])
