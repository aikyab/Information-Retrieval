

from os import listdir
from os.path import isfile, join

import os

import re
import collections

import nltk
from nltk.stem import PorterStemmer

nltk.download('stopwords')

def tokenize():
    mypath = f"/Users/aikyab/CS494/citeseer"
    os.chdir(mypath)
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    list_text = []
    regex_EXP = re.compile(r'[^\W\d]+')
    for path in onlyfiles:
        with open(path,encoding="latin-1") as f:
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

word_list = tokenize()

def totalNumOfWords(word_list):
    return len(word_list)

def numOfUniqueWords(word_list):
    unique_words = collections.Counter(word_list)
    return len(unique_words)

def topTwentyWords(word_list):
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

def stopWords(word_list):
    top_words = topTwentyWords(word_list)
    list_from_top = []
    stop_words = nltk.corpus.stopwords.words("english")
    dict_stop_words = collections.Counter(stop_words)
    for word_tuple in top_words:
        if dict_stop_words[word_tuple[0]]>0 :
            list_from_top.append(word_tuple[0])
    if not list_from_top:
        return "None"
    return list_from_top

def minimumWordsFor15Percent(word_list):
    total_words = totalNumOfWords(word_list)
    fifteen_percent = 0.15*total_words
    unique_words = collections.Counter(word_list)
    val_list = list(unique_words.values())
    key_list = list(unique_words.keys())
    count_freq = words = 0
    while count_freq<fifteen_percent:
        max_word_freq = max(val_list)
        position = val_list.index(max_word_freq)
        count_freq+=max_word_freq
        words+=1
        val_list.pop(position)
        key_list.pop(position)
    return words

print("Total Number of Words : ",totalNumOfWords(word_list))

print("Total Number of Unique words : ",numOfUniqueWords(word_list))

print("The top twenty words (along with their frequencies) are : ",topTwentyWords(word_list))

print("Stop words from the above list are",stopWords(word_list))

print(minimumWordsFor15Percent(word_list)," words account for 15% of the total words")

def stemmerStopEliminator():
    stop_words = nltk.corpus.stopwords.words("english")
    dict_stop_words = collections.Counter(stop_words)
    new_words = []
    
    ps = PorterStemmer()
    
    for word in word_list:
        if dict_stop_words[word]==0:
            new_words.append(ps.stem(word))
    return new_words

stemmed_words = stemmerStopEliminator()

print("Answers to questions \'a' through \'e' after stemming all words and eliminating the stop words --")

print("Total Number of Words : ",totalNumOfWords(stemmed_words))

print("Total Number of Unique words : ",numOfUniqueWords(stemmed_words))

print("The top twenty words (along with their frequencies) are : ",topTwentyWords(stemmed_words))

print("Stop words from the above list are",stopWords(stemmed_words))

print(minimumWordsFor15Percent(stemmed_words)," words account for 15% of the total words")
