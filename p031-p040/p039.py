from collections import defaultdict

#brute force
def p39solution1() -> int:
    perimeterDict = defaultdict(int)
    for a in range(1, 333):
        for b in range(a+1, 500):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c):
                perimeterDict[a+b+int(c)] += 1
    maxValue = 0
    maxKey = 0
    for key, value in perimeterDict.items():
        if value > maxValue:
            maxValue = value
            maxKey = key
    return maxKey

if __name__ == "__main__":
    print(p39solution1())