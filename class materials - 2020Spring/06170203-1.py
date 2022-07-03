#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:24:02 2020

@author: liuqingxuan
"""

import numpy as np
from numpy.linalg import inv
num = int(input("輸入矩陣大小："))
N = np.random.randint(100,size=(num,num)) #找整數亂數(介於0~99)
#N = np.array([[1,2,3],[4,5,6],[7,8,9]]) #測試三階矩陣
#N = np.array([[2,3],[2,3]]) #測試二階矩陣
print(int(np.linalg.det(N)))
while int(np.linalg.det(N))==0: #判斷是否為可逆矩陣，若不可逆，再找一個新的
    N = np.random.randint(100,size=(num,num)) #找整數亂數(介於0~99)
print(int(np.linalg.det(N)))

inv_N=inv(N) #計算M的反矩陣
#inv_N = np.linalg.inv(N) ＃計算反矩陣的另一種寫法
print("可逆的nxn方陣A:\n",N)
print("反矩陣B:\n",inv_N)
print(N.dot(inv_N)) #反矩陣與原矩陣相乘，得單位矩陣（1,0)(0,1)



#try:
#  N_inv = np.linalg.inv(N)
#  print(int(np.linalg.det(N)))
#except np.linalg.LinAlgError:
#  print('矩陣是不可逆矩陣')
#  N = np.random.randint(100,size=(3,3))



#try:
#    N_inv = np.linalg.inv(N)
#except np.linalg.LinAlgError:
#    print('矩陣是不可逆矩陣')
#    N = np.random.randint(100,size=(num,num)) #找整數亂數(介於0~99)
#    print(N)









