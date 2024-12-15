import primeHelperFunctions


def largest_consecutive_prime_sum(max: int) -> int:
    primes = primeHelperFunctions.primes_until_n(max)
    max_primes = 0
    max_sum = 0
    for i in range(len(primes)):
        temp_sum = 0
        for j in range(i, len(primes)):
            temp_sum += primes[j]
            if temp_sum > max:
                break
            if j - i + 1 < max_primes:
                continue
            if temp_sum in primes and j - i + 1 > max_primes:
                max_primes = j - i + 1
                max_sum = temp_sum
    return max_sum


if __name__ == "__main__":
    print(largest_consecutive_prime_sum(1000))
