# note that 9 digit pandigital primes cannot exist
# 1+2+3+4+5+6+7+8+9 = 45, divisible by 3
# similar with 8 digit pandigital primes
# there are no 1, or 2 digit pandigital primes by force. (1 is not a prime, nor is 12 or 21.)

import miscHelperFunctions
import primeHelperFunctions


def find_pandigital_primes() -> list[int]:
    pandigital_primes = []
    primes = primeHelperFunctions.primes_until_n(10 ** 8)
    print("Primes prepared")
    for prime in primes:
        if miscHelperFunctions.is_pandigital([prime], False, len(str(prime))):
            pandigital_primes.append(prime)
    return pandigital_primes


def p41solution1() -> int:
    return max(find_pandigital_primes())


if __name__ == "__main__":
    print(p41solution1())
