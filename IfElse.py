#!/bin/python3

N = int(input())

if N%2 == 0 and N == 2 or N == 4 or N > 20:
    print('Not Weird')
else:
    print('Weird')
