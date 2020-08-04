# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:45:01 2020

@author: AE401
"""

import random
Ans= random.randint(1,20)
t=0
while t<=5:
    num=input("請輸入1~20的數字")
    num=int(num)
    if num>=1 and 20>=num:
        if num==Ans:
            print("答對了!")
            print("你答了",t,"次")
            break
        elif num>Ans:
            print("小一點!")
            t=t+1
        else:
            print("大一點!")
            t=t+1
            
    else:
        print("......!?")
