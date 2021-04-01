# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:27:29 2020

@author: dell
"""

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    a=int(s[:2])
    if 'PM'==s[-2:]:
        a=str(12+a)
    s1=s.replace(s[0],a[0])
    s1=s1.replace(s1[1],a[1])
    s1=s1[:-2]
    print(s1)
if __name__ == '__main__':
    s = input()
    timeConversion(s)
