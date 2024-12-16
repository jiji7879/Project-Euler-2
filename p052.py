def p52solution1():
    # smallest number where digits of x = digits of 2x is 125874
    i = 125874
    while True:
        digits = list(str(i))
        digits.sort()
        digits2 = list(str(2 * i))
        digits2.sort()
        digits3 = list(str(3 * i))
        digits3.sort()
        digits4 = list(str(4 * i))
        digits4.sort()
        digits5 = list(str(5 * i))
        digits5.sort()
        digits6 = list(str(6 * i))
        digits6.sort()
        if digits == digits2 and digits == digits3 and digits == digits4 and digits == digits5 and digits == digits6:
            return i
        i += 1


if __name__ == "__main__":
    print(p52solution1())
