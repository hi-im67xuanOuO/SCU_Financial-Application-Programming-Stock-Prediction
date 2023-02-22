#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:34:08 2020

@author: liuqingxuan
"""
import re

abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print (email)

emails = re.findall(r'@[\w\.-]+',abc)
for email in emails:
    print(email)    