# You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
# 
# A valid credit card from ABCD Bank has the following characteristics: 
# 
# ► It must start with a 4,5 or 6. 
# ► It must contain exactly 16 digits. 
# ► It must only consist of digits (0-9). 
# ► It may have digits in groups of 4, separated by one hyphen "-". 
# ► It must NOT use any other separator like ' ' , '_', etc. 
# ► It must NOT have 4 or more consecutive repeated digits.
# https://www.hackerrank.com/contests/pythonist3/challenges/validating-credit-card-number

from itertools import groupby

def checkValidity(num):
    if(num.count("-") > 3):
        return "Invalid";
    
    num_without_hyphen = num.replace("-", "");
    
    if(len(num_without_hyphen) != 16):
        return "Invalid";
    
    if(num[0] not in ['4', '5', '6']):
        return "Invalid";
    
    if(not num_without_hyphen.isdigit()):
        return "Invalid";
    
    for i in range(len(num)):
        if(num[i] == "-" and i not in [4, 9, 14]):
            return "Invalid"
    
    groups = groupby(num_without_hyphen)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    result = [(x, y) for x, y in result if y >= 4]

    if(len(result) != 0):
        return "Invalid"
    
    return "Valid"
    
def main():
    print(checkValidity("61236-567-8912-3456"))
    
if(__name__ == "__main__"):
    main();
