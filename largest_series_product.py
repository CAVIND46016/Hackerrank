#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem
# This problem is a programming version of Problem 8 from projecteuler.net

import sys
from operator import mul
from functools import reduce

def k_prod(n, k, num):
    num = list(map(int, str(num)))
    sub_arr = []
    for i in range(n-k+1):
        sub_arr.append(reduce(mul, num[i:k+i], 1));
        
    return max(sub_arr)


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(k_prod(n, k, num))
