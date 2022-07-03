#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:46:03 2020

@author: liuqingxuan
"""

import re
import requests
the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def get_book(url):
    # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Discards the metadata from the beginning of the book
    start = re.search(r"PART I",raw ).end()
    # Discards the metadata from the end of the book 起始
    stop = re.search(r"II", raw).start()
    # Keeps the relevant text  結尾
    text = raw[start:stop]
    return text

def preprocess(sentence): 
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower() #只抓大小寫英文字母數字與句點，其他符號會不見

book = get_book(the_idiot_url)
processed_book = preprocess(book)
print(processed_book)

print(len(re.findall(r'the', processed_book))) #Find the number of "the" 

letters = re.findall(r'[a-zA-Z0-9]*--[a-zA-Z0-9]*', book) #Find the words connected by '--'
for x in letters:
    print(x)
print(len(re.findall(r'--', book))) #Find the number of "--" 