# https://www.hackerrank.com/challenges/fibonacci-modified
import sys

def mod_FIBO(list_fib, n):
    a, b = list_fib[0], list_fib[1]
    m = list_fib
    for i in range(0, 21):
        a, b = b, a + b*b
        if(i == 0):
            continue;
        m.append(a)
    return m[n-1]

first, second, n = input().strip().split(' ')
first, second, n = [int(first), int(second), int(n)]
list_fib = []

list_fib.append(first);
list_fib.append(second);
print(mod_FIBO(list_fib, n))
