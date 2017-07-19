# Week of code 27 challenge 
# https://www.hackerrank.com/contests/w27/challenges/drawing-book

import sys
def getMinNumOfPages(n, p):
    numOfPages_front = p // 2;
    numOfPages_back = (n - p) // 2;
    if(numOfPages_front < numOfPages_back):
        return numOfPages_front;
    else:
        return numOfPages_back;
    
n = int(input().strip())
p = int(input().strip())
print(getMinNumOfPages(n, p))
