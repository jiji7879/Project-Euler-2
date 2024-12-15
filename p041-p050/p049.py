from collections import defaultdict

import primeHelperFunctions


def prime_permutations_four_digits() -> list:
    primes = primeHelperFunctions.primes_until_n(10000)
    dictOfPermutations = defaultdict(list)
    solutionList = []
    for prime in primes:
        if len(str(prime)) <= 3:
            continue
        digits = list(str(prime))
        digits.sort()
        digits_string = ""
        for x in digits:
            digits_string += x
        dictOfPermutations[digits_string].append(prime)
    dict_of_three_plus_permutations = {}
    for key, value in dictOfPermutations.items():
        if len(value) >= 3:
            dict_of_three_plus_permutations[key] = value
    for prime_permutations in dict_of_three_plus_permutations.values():
        for i in range(len(prime_permutations) - 1):
            for j in range(i + 1, len(prime_permutations)):
                diff = prime_permutations[j] - prime_permutations[i]
                if prime_permutations[j] + diff in prime_permutations:
                    solutionList.append([prime_permutations[i], prime_permutations[j], prime_permutations[j] + diff])
    return solutionList


if __name__ == "__main__":
    print(prime_permutations_four_digits())
