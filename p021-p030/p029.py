import primeHelperFunctions


def distinct_powers(a: int, b: int) -> int:
    primes = primeHelperFunctions.primes_until_n(b + 1)
    distinctPowers = 0
    for base in range(2, a + 1):
        distinctPowers += b - 1
        if base ** 2 > a:
            continue
        for exponent in range(2, b + 1):
            if exponent not in primes:
                divisors = primeHelperFunctions.divisor_list(exponent, primes)
                for i in range(1, len(divisors) - 1):
                    if base ** divisors[i] <= a and divisors[-i - 1] <= b:
                        distinctPowers -= 1
                        break
            else:
                if base ** exponent > a:
                    continue
    return distinctPowers


def distinct_powers_brute_force(a: int, b: int) -> int:
    setOfDistinctPowers = set()
    for base in range(2, a + 1):
        for exponent in range(2, b + 1):
            setOfDistinctPowers.add(base ** exponent)
    return len(setOfDistinctPowers)


if __name__ == "__main__":
    # print(distinct_powers(100, 100))
    print(distinct_powers_brute_force(100, 100))
