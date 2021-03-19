#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 1
    jumpCount = 0
    while i < len(c):
        print("i at top " + str(i))
        print("length c " + str(len(c)))
        if i !=len(c)-1:
            if c[i+1]==0:
                i+=2
                jumpCount+=1
            elif c[i]==0:
                i+=1
                jumpCount+=1
        else:
            i+=1
            jumpCount +=1
    return jumpCount


    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

  
