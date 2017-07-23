# https://www.hackerrank.com/challenges/ctci-lonely-integer

from collections import Counter

def lonely_integer(a):
    return sorted(Counter(a).items(), key=lambda i: i[1])[0][0];

def main():
    n = 5
    a = [0, 0, 1, 2, 1];
    print(lonely_integer(a))
    
if(__name__ == "__main__):
    main();
