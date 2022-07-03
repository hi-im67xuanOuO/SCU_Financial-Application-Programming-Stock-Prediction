#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:42:50 2020

@author: liuqingxuan
"""

import numpy as y
a = y.array([[1,2,3],[4,5,6]])
print(y.size(a)) #a裡面有總共幾個項目
print(y.size(a,0)) #a的每一個直行有幾個項目
print(y.size(a,1)) #a的每一個橫列有幾個項目
print(y.shape(a)) #a是幾乘幾的矩陣（行數,列數）

import numpy as np
L = np.random.random(10) #找10個0~1的亂數
print(L)
print(sum(L)) #印出這10個亂數的總和

M = np.random.random((3,4)) #找4*3個0~1的亂數
print(M)
print(M.sum()) #亂數的總和
print(M.min(axis=0)) #每一直行的最小值
print(M.min(axis=1)) #每一橫列的最小值
print(M.max(axis=0)) #每一直行的最大值
print(M.max(axis=1)) #每一橫列的最大值
print(M.sum(axis=0)) #每一直行的總和
print(M.sum(axis=1)) #每一橫列的總和
print(M.min())

M = np.random.randint(10,size=(3,4)) #找4*3個整數亂數(介於0~9)
print(M)
print(M.sum()) #亂數的總和
print(M.min(axis=0)) #每一直行的最小值
print(M.min(axis=1)) #每一橫列的最小值
print(M.max(axis=0)) #每一直行的最大值
print(M.max(axis=1)) #每一橫列的最大值
print(M.sum(axis=0)) #每一直行的總和
print(M.sum(axis=1)) #每一橫列的總和
print(M.min())


from numpy.linalg import inv
a = np.arange(16).reshape(4,4) #arange是從0到15「依序」形成4*4的矩陣
print(a)
M = np.array([[2,3],[5,7]])
print(M)
invM=inv(M) #計算M的反矩陣
print(invM)
print(M.dot(invM)) #反矩陣與原矩陣相乘，得單位矩陣（1,0)(0,1)
print(M.dot((1,1))) #反矩陣與（1,1)矩陣相乘，得新矩陣