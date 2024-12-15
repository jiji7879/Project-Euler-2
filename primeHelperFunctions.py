# done in p7
# uses sieve of eratosthenes
def first_n_primes(number_of_prime_targets: int) -> list[int]:
    primeList = []
    # target number is n*ln(n) by prime number theorem, which is an overestimate
    # we can estimate log_10(n) by counting the number of digits, then add 1 to overestimate
    # Since we want ln(n)=log_e(n), use the change of base formula.
    # So ln(n) = log(n)/log(e). Note that 1/log(e) is around 2.303.
    # Let's round it up to 3 because there's also some weird stuff going on with the log function.
    targetNumber = number_of_prime_targets * (len(str(number_of_prime_targets)) + 1) * 3
    listOfNumbers = [False] * (targetNumber + 1)
    for i in range(2, int((targetNumber + 1) ** 0.5)):
        if not listOfNumbers[i]:
            primeList.append(i)
            if len(primeList) == number_of_prime_targets:
                return primeList
            for j in range(i, targetNumber + 1, i):
                listOfNumbers[j] = True
    for i in range(int((targetNumber + 1) ** 0.5), targetNumber + 1):
        if not listOfNumbers[i]:
            primeList.append(i)
            if len(primeList) == number_of_prime_targets:
                return primeList
    return primeList


# done in p10
# uses sieve of eratosthenes
def primes_until_n(limit: int) -> list[int]:
    if limit == 2:
        return [2]
    elif limit == 3:
        return [2, 3]
    elif limit <= 6:
        return [2, 3, 5]
    elif limit <= 10:
        return [2, 3, 5, 7]
    primeList = []
    listOfNumbers = [False] * (limit + 1)
    for i in range(2, int((limit + 1) ** 0.50) + 1):
        if not listOfNumbers[i]:
            primeList.append(i)
            for j in range(i, limit + 1, i):
                listOfNumbers[j] = True
    for i in range(int((limit + 1) ** 0.50) + 1, limit + 1):
        if not listOfNumbers[i]:
            primeList.append(i)
    return primeList


# def primes_until_n2(limit: int) -> list:
#     primeList = []
#     listOfNumbers = [False] * (limit + 1)
#     for i in range(2, limit+1):
#         if not listOfNumbers[i]:
#             primeList.append(i)
#             for j in range(i, limit + 1, i):
#                 listOfNumbers[j] = True
#     return primeList
#
# def primes_until_n3(limit: int) -> list:
#     primeList = []
#     listOfNumbers = [False] * (limit + 1)
#     for i in range(2, limit+1):
#         if not listOfNumbers[i]:
#             primeList.append(i)
#             if i < (limit + 1) // i:
#                 for j in range(i, limit + 1, i):
#                     listOfNumbers[j] = True
#     return primeList

# done in p12
# returns a dictionary that maps unique primes to their multiplicities
def prime_factors(n: int, list_of_potential_primes: list[int] = None) -> dict[int, int]:
    if list_of_potential_primes is None:
        list_of_potential_primes = primes_until_n(n)
    dictOfPrimeFactors = {}
    for i in list_of_potential_primes:
        if i > n:
            break
        j = 0
        while n % i == 0:
            n = n // i
            j += 1
        if j > 0:
            dictOfPrimeFactors[i] = j
    return dictOfPrimeFactors


# done in p12
def number_of_divisors(n: int, list_of_potential_primes: list[int] = None) -> int:
    prime_factor_list = prime_factors(n, list_of_potential_primes)
    return number_of_divisors_from_dict(prime_factor_list)


def number_of_divisors_from_dict(dict_of_prime_factors: dict[int, int]) -> int:
    divisors = 1
    for prime in dict_of_prime_factors:
        divisors *= (dict_of_prime_factors[prime] + 1)
    return divisors


# done in p12
# By Fundamental Theorem of Arithmetic, these will multiply to unique integers
def multiply_prime_factors(dict_of_prime_factors1: dict[int, int], dict_of_prime_factors2: dict[int, int]) -> dict[
    int, int]:
    for prime in dict_of_prime_factors1:
        if prime in dict_of_prime_factors2:
            dict_of_prime_factors2[prime] = dict_of_prime_factors2[prime] + dict_of_prime_factors1[prime]
        else:
            dict_of_prime_factors2[prime] = dict_of_prime_factors1[prime]
    return dict_of_prime_factors2


# done in p21
def divisor_list(n: int, list_of_potential_primes: list[int] = None) -> list[int]:
    if n == 1:
        return [1]
    prime_factor_dict = prime_factors(n, list_of_potential_primes)
    return divisors_from_dict(prime_factor_dict)


def divisors_from_dict(dict_of_prime_factors: dict[int, int]) -> list[int]:
    divisors: list = [1]
    for prime in dict_of_prime_factors:
        new_divisors = []
        for divisor in divisors:
            for power in range(1, dict_of_prime_factors[prime] + 1):
                new_divisors.append(divisor * (prime ** power))
        divisors = divisors + new_divisors
    divisors.sort()
    return divisors


# totient(m) * totient(n) = totient(m * n) if m and n are relatively prime
# Chinese Remainder Theorem
# Each prime power is relatively prime to each other so long as the primes are distinct
#
# On the totient of a prime power:
# Note that exactly p^k/p = p^(k-1) numbers will divide p
# So totient(p^k) = p^k - p^k/p = (p-1)/p p^k = (p-1) p^(k-1) = (1-1/p) p^k
# Multiplying all the primes will give totient(n) = n * (1-1/p_1) * (1-1/p_2)...
def totient(n: int, list_of_potential_primes: list[int] = None) -> int:
    if n == 1:
        return 1
    totient_num = n
    prime_dicts = prime_factors(n, list_of_potential_primes)
    for prime in prime_dicts.keys():
        totient_num = (prime - 1) * totient_num // prime
    return totient_num


def gcd(num1: int, num2: int, list_of_potential_primes: list[int] = None) -> int:
    num1_prime_factor_dict = prime_factors(num1, list_of_potential_primes)
    num2_prime_factor_dict = prime_factors(num2, list_of_potential_primes)
    gcd_num = 1
    for power in num1_prime_factor_dict:
        if power in num2_prime_factor_dict:
            gcd_num *= power ** min(num1_prime_factor_dict[power], num2_prime_factor_dict[power])
    return gcd_num
