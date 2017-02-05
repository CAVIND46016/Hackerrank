# Week of code 27 challenge 
# https://www.hackerrank.com/contests/w27/challenges/drawing-book

import sys

def numOfPages_front(n, p):
    return (p // 2);

def numOfPages_back(n, p):
    return (n - p) // 2;
    
def getMinNumOfPages(n, p):
    if(numOfPages_front(n, p) < numOfPages_back(n, p)):
        return numOfPages_front(n, p);
    else:
        return numOfPages_back(n, p);
    
n = int(input().strip())
p = int(input().strip())
print(getMinNumOfPages(n, p))
