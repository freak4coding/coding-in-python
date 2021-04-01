# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:09:08 2020

@author: dell
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    a = b = 0
    for i in range(len(arr)-1):
        a+=arr[i]
    for i in range(1,len(arr)):
        b+=arr[i]
    print(str(a) + " " + str(b))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
