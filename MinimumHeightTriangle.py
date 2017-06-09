# https://www.hackerrank.com/contests/infinitum18/challenges/lowest-triangle
# Given integers 'b' and 'a', find the smallest integer 'h' , such that there exists a triangle of height 'h', base 'b', 
# having an area of at least 'a'.


import sys
import math

def lowestTriangle(base, area):
    return math.ceil(2*area/base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
