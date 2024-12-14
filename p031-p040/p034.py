FAST_FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


# brute force
# note that 7 * 9! = 2540160, so that is the max.
def p34solution1() -> int:
    sum1 = 0
    for i in range(3, 2540160):
        factorial_sum = 0
        for j in str(i):
            factorial_sum += FAST_FACTORIAL[int(j)]
        if factorial_sum == i:
            sum1 += i
    return sum1


if __name__ == "__main__":
    print(p34solution1())
