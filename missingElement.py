#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result=[]
    for i in range(len(grades)):
        if grades[i] < 38 and grades[i]%5 == 0:
            result.append(grades[i])
        else:
            gr=grades[i]
            c = 0
            while grades[i] % 5 != 0:
                c+=1
                grades[i]+=1
            if c<3:
                result.append(grades[i])
            else:
                result.append(grades[i]-c)
    return result


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
