import primeHelperFunctions


def goldbach_other_conjecture() -> int:
    k = 5
    odd_sum = 9
    while True:
        limit = 10 ** k
        primes = primeHelperFunctions.primes_until_n(limit)
        while odd_sum < limit:
            if odd_sum in primes:
                odd_sum += 2
                continue
            square = 1
            temp_solution_found = False
            while temp_solution_found == False and 2 * square ** 2 < odd_sum:
                if odd_sum - (2 * square ** 2) in primes:
                    temp_solution_found = True
                square += 1
            if not temp_solution_found:
                return odd_sum
            else:
                odd_sum += 2
        k += 1


if __name__ == "__main__":
    print(goldbach_other_conjecture())
