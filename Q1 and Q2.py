# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 07:37:58 2020

@author: beaka
"""
## Question 1

numbers=[] 
for x in range(2000, 3200):
    if (x%7==0) and (x%5 != 0):
       numbers.append(x)
print (numbers) 


#Question 2

class Input_file:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input()

    def print_String(self):
        print(self.s.upper())

strObj = Input_file()
strObj.get_String()
strObj.print_String()


