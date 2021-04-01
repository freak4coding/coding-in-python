#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                sum1+=arr[i][j]
    c=1
    for l in range(len(arr)):
        for m in range(len(arr)):
            if m==len(arr)-c:
                sum2+=arr[l][len(arr)-c]
                c+=1
    return abs(sum1-sum2)

if __name__ == '__main__':

    n = int(input("Enter the matrix size : ").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(f"result = {result}")