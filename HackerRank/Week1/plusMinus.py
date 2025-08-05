#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    plus =0
    minus=0
    zeros=0
    
    for i in arr:
        if i>0:
            plus=plus+1
        elif i<0:
            minus =minus+1
        else:
            zeros =zeros+1
            
    total = len(arr)
    print(round(plus / total,6))
    print(round(minus / total,6))
    print(round(zeros / total,6))
    
    
if __name__ == '__main__':
    n=int(input())
    arr = list(map(int,input().rstrip().split()))
    plusMinus(arr)
    
    
    
    
    
    
    
