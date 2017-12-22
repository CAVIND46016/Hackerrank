#!/bin/python3
# https://www.hackerrank.com/challenges/2d-array/problem

import sys
import operator

def max_hourglass_sum(arr):
    sub_arrs = dict();
    for i in range(1, 5):
        for j in range(1, 5):
            sub_arrs[str(i) + str(j)] = sum(arr[i-1][(j-1):(j+2)]) + arr[i][j] + sum(arr[i+1][(j-1):(j+2)])
 
    return max(sub_arrs.items(), key=operator.itemgetter(1))[1];
    

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
print(max_hourglass_sum(arr))
