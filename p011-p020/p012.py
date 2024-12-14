import primeHelperFunctions


def triangle_number(n: int) -> int:
    # Note that triangle number n is 1+2+...+n
    # By Gauss, pair n and 1, n-1 and 2, etc. n/2 times
    # Easy way is n*(n+1)/2. We can safely // because either n or n+1 is even.
    return n * (n + 1) // 2


def p12solution1() -> int:
    listOfPotentialPrimes = primeHelperFunctions.primes_until_n(1000000)
    divisors = 1
    i = 2
    while divisors < 500:
        divisors = primeHelperFunctions.number_of_divisors(triangle_number(i), listOfPotentialPrimes)
        i += 1
    return divisors


def p12solution2() -> int:
    listOfPotentialPrimes = primeHelperFunctions.primes_until_n(1000000)
    divisors = 1
    i = 2
    while divisors < 500:
        divisorsList1 = primeHelperFunctions.prime_factors(i + 1, listOfPotentialPrimes)
        divisorsList2 = primeHelperFunctions.prime_factors(i, listOfPotentialPrimes)
        mult = primeHelperFunctions.multiply_prime_factors(divisorsList1, divisorsList2)
        mult[2] = mult[2] - 1
        divisors = primeHelperFunctions.number_of_divisors_from_dict(mult)
        i += 1
    return divisors

if __name__ == "__main__":
    print(p12solution1())