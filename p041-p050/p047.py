import primeHelperFunctions


def find_consec_distinct_prime_factors(num_consec: int, num_distinct_primes: int) -> int:
    if num_distinct_primes <= 0 or num_consec <= 0:
        return 0
    if num_distinct_primes == 1:
        return 2 if num_consec <= 2 else 0
    log_exponent = 2
    smallest_number = 2
    while True:
        print(log_exponent)
        max_num = 10 ** log_exponent
        primes = primeHelperFunctions.primes_until_n(max_num)
        while smallest_number + num_consec < max_num:
            if smallest_number in primes or len(
                    primeHelperFunctions.prime_factors(smallest_number, primes)) != num_distinct_primes:
                smallest_number += 1
                continue
            solution_found = True
            for i in range(num_consec):
                if smallest_number + i in primes or len(
                        primeHelperFunctions.prime_factors(smallest_number + i, primes)) != num_distinct_primes:
                    solution_found = False
                    break
            if solution_found:
                return smallest_number
            else:
                smallest_number += 1
        log_exponent += 1


if __name__ == "__main__":
    print(find_consec_distinct_prime_factors(4, 4))
