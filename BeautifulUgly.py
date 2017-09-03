# https://www.hackerrank.com/contests/codeagon/challenges/ugly-or-beautiful/problem

import sys

def isUnique(a):
    if(len(list(set(a))) == len(a)):
        return True;
    
    return False;
    
def isAscending(a):
    n = len(a)
    for i in range(n):    
        for j in range(0, n - i - 1):
            if(a[j] > a[j+1]):
                return True;
                
        return False;
    
def valueConstraint(a):
    if(max(a) == len(a)):
        return True;
    
    return False;

def uglyOrBeautiful(a):
    if(isUnique(a) and isAscending(a) and valueConstraint(a)):
        return "Beautiful";
    
    return "Ugly";

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        result = uglyOrBeautiful(a)
        print(result)
