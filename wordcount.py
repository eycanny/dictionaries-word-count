"""Count words in file."""
import sys

input_file = open(sys.argv[1])

# def word_count(input_file):

word_counts = {}
    
    # file = open(input_file)
    
for line in input_file:
    line = line.rstrip()
    word_list = line.split(" ")

    for word in word_list:
        word_counts[word] = word_counts.get(word,0) + 1
    
input_file.close()

for word in word_counts:
    print(word, word_counts[word])
