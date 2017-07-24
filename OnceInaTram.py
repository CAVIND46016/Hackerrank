# https://www.hackerrank.com/contests/w34/challenges/once-in-a-tram

def luckyNumber(num):
    sf3 = sum([int(i) for i in str(num)[:3]]);
    sl3 = sum([int(i) for i in str(num)[3:]]);
    return (sf3 == sl3);

def onceInATram(x):
    x = x + 1;
    while(True):
        if(luckyNumber(x)):
            break;
        x = x + 1;
        
    return x;

if __name__ == "__main__":
    x = 555555
    result = onceInATram(x)
    print(result)
