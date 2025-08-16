#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def pangrams(s):
    alphabet = {}
    for i in s.lower():
        if i.isalpha() and i in alphabet:
            alphabet[i] += 1
        elif i.isalpha() and i not in alphabet:
            alphabet[i] = 0
    
    if len(alphabet) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
