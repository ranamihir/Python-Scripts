import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    text_file = open(url, 'r+')
    words = text_file.read().split()
    for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)
    
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "”~!@#$%^&*()—_+{}|:\"‘<>?/“….,';\’][=-`"
        useless_words = []
        for i in range(0, len(symbols)):
            word = word.lower()
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)
    
    
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)
        fw.write(str(key) + ' ' + str(value) + '\n')

fw = open('result_file.txt', 'w')            
start('input_file.txt')
fw.close()