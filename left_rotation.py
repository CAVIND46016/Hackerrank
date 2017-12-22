#!/bin/python3
# https://www.hackerrank.com/challenges/array-left-rotation/problem

import sys

def leftRotation(a, d):
    for i in range(d):
        f = a[0]
        a = a[1:len(a)] + [f];
        
    return a;

ip_arr = [1, 2, 3, 4, 5];

print(leftRotation(ip_arr, 5))
