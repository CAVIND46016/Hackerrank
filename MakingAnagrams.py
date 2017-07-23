# https://www.hackerrank.com/challenges/ctci-making-anagrams

from collections import Counter

def number_needed(a, b):
    ca = Counter(a);
    cb = Counter(b);
    ca.subtract(cb);
    return sum(abs(val) for val in ca.values());

def main():
    a = input().strip();
    b = input().strip();

if(__name__ == "__main__"):
    print(number_needed(a, b));
