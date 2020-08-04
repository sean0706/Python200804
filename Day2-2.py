# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:22:55 2020

@author: AE401
"""
import random
Ans= random.randint(1,20)
while True:
    num=input("請輸入1~20的數字")
    num=int(num)
    if num>=1 and 20>=num:
        if num==Ans:
            print("答對了!")
            break
        elif num>Ans:
            print("小一點!")
        else:
            print("!")
            
    else:
        print("......!?")

        
