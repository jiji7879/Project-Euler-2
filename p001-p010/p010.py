import primeHelperFunctions


def p10solution1() -> int:
    return sum(primeHelperFunctions.primes_until_n(2000000))


if __name__ == "__main__":
    print(p10solution1())
