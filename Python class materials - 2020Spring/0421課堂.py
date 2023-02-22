#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:31:20 2020

@author: liuqingxuan
"""

import re
pattern = 'Cookie'
str="... Cookie ... Cookies guru98, education is fun"
if re.match(pattern,str):
    print("Match!")
else:
    print("Not a match")
print(re.match(pattern,str,flags=0))
print(re.findall(pattern,str)) #符合pattern的印出
print(re.findall(r'\d',str)) #找數字
print(re.findall(r'\w',str)) #字母不含數字
print((re.split(r'\s',str))) #空白鍵切割
print((re.split(r's',str))) # There is no s