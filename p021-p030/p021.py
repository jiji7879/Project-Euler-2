import primeHelperFunctions


def p21solution(max_num: int) -> int:
    divisorSums = {}
    sum1 = 0
    primes = primeHelperFunctions.primes_until_n(max_num + 1)
    for i in range(1, max_num + 1):
        divisor_sum = sum(primeHelperFunctions.divisor_list(i, primes)) - i
        divisorSums[i] = divisor_sum
        if i != divisor_sum and divisor_sum in divisorSums and divisorSums[divisor_sum] == i:
            if divisor_sum < 10000:
                sum1 += divisor_sum
            sum1 += i
    return sum1


if __name__ == "__main__":
    print(p21solution(10000))
