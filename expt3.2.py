# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 04:18:49 2026

@author: amruta jadhav
"""
year=int(input("enter year."))
if(year % 400==0) or (year%4==0and year % 100!=0):
print("leap year")
else:
    print("not a leap year")
