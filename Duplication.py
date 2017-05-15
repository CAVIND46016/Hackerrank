# https://www.hackerrank.com/contests/w32/challenges/duplication  ==> Week of Code 32

import sys
import math

def complement(s):
    t = []
    for i in range(len(s)):
        if(s[i] == "0"):
            t.append("1")
        else:
            t.append("0");
            
    return ''.join(t);

def getSeries():
    t = "0";
    for i in range(1, int(math.log(1000, 2)) + 1):
        t = t + complement(t)

    return t;

t = getSeries()
q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    print(t[x])
