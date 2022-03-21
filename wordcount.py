"""Count words in file."""


# put your code here.
def word_count(file_name):

    word_counts = {}
    
    file = open(file_name)
    
    for line in file:
        line = line.rstrip()
        word_list = line.split(" ")

        for word in word_list:
            word_counts[word] = word_counts.get(word,0) + 1
    
    file.close()

    return word_counts