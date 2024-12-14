import primeHelperFunctions


# brute force
def p37solution1() -> int:
    # guess
    primes = primeHelperFunctions.primes_until_n(1000000)
    truncated_primes = []
    k = 1
    for prime in primes:
        if prime > k * 100000:
            print(k * 100000)
            k += 1
        if len(truncated_primes) == 11:
            break
        if str(prime)[0] in {2, 4, 6, 8} or prime < 10:
            continue
        prime_list = list(str(prime))
        right_truncated = ""
        is_truncated_prime = True
        for i in range(len(prime_list)):
            right_truncated += prime_list[i]
            if int(right_truncated) not in primes:
                is_truncated_prime = False
                break
        if not is_truncated_prime:
            continue
        is_truncated_prime = True
        left_truncated = ""
        for i in range(len(prime_list)):
            left_truncated = prime_list[-i - 1] + left_truncated
            if int(left_truncated) not in primes:
                is_truncated_prime = False
                break
        if not is_truncated_prime:
            continue
        truncated_primes.append(prime)
    print(truncated_primes)
    print(len(truncated_primes))
    return sum(truncated_primes)


if __name__ == "__main__":
    print(p37solution1())
