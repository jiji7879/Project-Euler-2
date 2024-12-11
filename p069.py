import primeHelperFunctions

def p69solution1(max_int: int) -> int:
    primes = helperFunctions.primes_until_n(max_int)
    max_quotient = 0
    max_number = 0
    for i in range(2, max_int, 2):
        if i % 10000 == 0:
            print(i)
        quotient = i/helperFunctions.totient(i, primes)
        if quotient > max_quotient:
            max_quotient = quotient
            max_number = i
    return max_number


if __name__ == "__main__":
    print(p69solution1(1000000))