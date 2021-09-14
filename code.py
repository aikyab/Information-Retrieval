from os import listdir
from os.path import isfile, join

import re
import collections

def tokenize():
    mypath = f"/Users/aikyab/citeseer"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    list_text = []
    regex_EXP = re.compile(r'[^\W\d]+')
    for path in onlyfiles:
        with open(path) as f:
            text = f.read()
            word_match=regex_EXP.finditer(text)
            words = []
            for i in word_match:
                words.append(i.group())
            tokens = [word for word in words]
            list_text += tokens
    trimmed_words = []
    for word in list_text:
        if len(word)==1:
            if ord(word.lower())==97 or ord(word.lower())==105:
                trimmed_words.append(word.lower())
        else:
            trimmed_words.append(word.lower())
    return trimmed_words

def totalNumOfWords():
    word_list = tokenize()
    return len(word_list)

def numOfUniqueWords():
    word_list = tokenize()
    unique_words = collections.Counter(word_list)
    return len(unique_words)

def topTwentyWords():
    word_list = tokenize()
    unique_words = collections.Counter(word_list)
    val_list = list(unique_words.values())
    key_list = list(unique_words.keys())
    top_words_list = []
    i = 0
    while i<20:
        max_word_freq = max(val_list)
        position = val_list.index(max_word_freq)
        word = key_list[position]
        top_words_list.append((word,max_word_freq))
        val_list.pop(position)
        key_list.pop(position)
        i+=1
    return top_words_list







# # print("Total Number of Words : "+str(totalNumOfWords()))

# # print("Total Number of Unique words : "+str(numOfUniqueWords()))

# print("The top twenty words are : ",topTwentyWords())

word_list = tokenize()
unique_words = collections.Counter(word_list)
print(max(unique_words.values()))


