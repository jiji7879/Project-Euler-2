import math

#done in p7
#uses sieve of eratosthenes
def first_n_primes(number_of_prime_targets: int) -> list:
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


#done in p10
#uses sieve of eratosthenes
def primes_until_n(limit: int) -> list:
    if limit == 2:
        return [2]
    elif limit == 3:
        return [2, 3]
    primeList = []
    listOfNumbers = [False] * (limit + 1)
    for i in range(2, int((limit + 1) ** 0.5)):
        if not listOfNumbers[i]:
            primeList.append(i)
            for j in range(i, limit + 1, i):
                listOfNumbers[j] = True
    for i in range(int((limit + 1) ** 0.5), limit + 1):
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


#done in p11
def read_file_as_array_of_numbers(filename: str) -> list:
    # open the file
    f = open(filename, "r")

    arrayOfNumbers = []
    #read each line
    for line in f:
        arrayOfNumbersInLine = []
        #split the line into an array of numbers
        for number in line.split():
            # put it in as a number
            arrayOfNumbersInLine.append(int(number))
        arrayOfNumbers.append(arrayOfNumbersInLine)
    return arrayOfNumbers

#done in p12
#returns a dictionary that maps unique primes to their multiplicities
def prime_factors(n: int, list_of_potential_primes: list = None) -> dict:
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
            dictOfPrimeFactors[i]=j
    return dictOfPrimeFactors


#done in p12
def number_of_divisors(n: int, list_of_potential_primes: list = None) -> int:
    primeFactorList = prime_factors(n, list_of_potential_primes)
    return number_of_divisors_from_dict(primeFactorList)

def number_of_divisors_from_dict(dict_of_prime_factors: dict) -> int:
    divisors = 1
    for prime in dict_of_prime_factors:
        divisors *= (dict_of_prime_factors[prime] + 1)
    return divisors

#done in p12
# By Fundamental Theorem of Arithmetic, these will multiply to unique integers
def multiply_prime_factors(dict_of_prime_factors1: dict, dict_of_prime_factors2: dict) -> dict:
    for prime in dict_of_prime_factors1:
        if prime in dict_of_prime_factors2:
            dict_of_prime_factors2[prime]= dict_of_prime_factors2[prime] + dict_of_prime_factors1[prime]
        else:
            dict_of_prime_factors2[prime]=dict_of_prime_factors1[prime]
    return dict_of_prime_factors2

# done in p15
# the polynomial list is structured from highest order to least
# for example, multiplying (x^2+1)(x^3-2x^2+x-1) correlates to [1,0,1] and [1,-2,1,-1]
def polynomial_multiplication(polynomial1: list, polynomial2: list) -> list:
    multiplication_result = [0 for _ in range(len(polynomial1)+len(polynomial2)-1)]
    for polynomial_2_term_index in range(len(polynomial2)):
        for polynomial_1_term_index in range(len(polynomial1)):
            multiplication_result[polynomial_1_term_index+polynomial_2_term_index] += (
                    polynomial1[polynomial_1_term_index] * polynomial2[polynomial_2_term_index])
    return multiplication_result

# done in p16
def big_number_multiplication(big_num1: list, big_num2: list, base: int = 10) -> list:
    multiplication_result = polynomial_multiplication(big_num1, big_num2)
    return big_number_carrying(multiplication_result, base)

# done in p25
def big_number_addition(big_num1: list, big_num2: list, base: int = 10) -> list:
    if len(big_num1) > len(big_num2):
        big_num2 = [0 for _ in range(len(big_num1)-len(big_num2))] + big_num2
    else:
        big_num1 = [0 for _ in range(len(big_num2) - len(big_num1))] + big_num1
    addition_result = [0 for _ in range(len(big_num1))]
    for i in range(len(big_num1)):
        addition_result[i] = big_num1[i] + big_num2[i]
    return big_number_carrying(addition_result, base)

def big_number_carrying(big_num_list: list, base: int) -> list:
    for negative_index in range(1, len(big_num_list)):
        if big_num_list[-negative_index] >= base:
            big_num_list[-negative_index - 1] += big_num_list[-negative_index] // base
            big_num_list[-negative_index] = big_num_list[-negative_index] % base
    while big_num_list[0] >= base:
        big_num_list.insert(0, big_num_list[0] // base)
        # the rest of the result should be pushed to the right by 1
        big_num_list[1] = big_num_list[1] % base
    return big_num_list

# done in p16
def digit_sum(num: int) -> int:
    num_string = str(num)
    digit_sum1 = 0
    for char in num_string:
        digit_sum1 += int(char)
    return digit_sum1

# done in p18, at least reused in p67
# the triangle_list assumes a list of ascending lengths increasing by exactly 1
# for example, the list from the p18 sample input should be [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
def path_sum(triangle_list: list) -> int:
    for i in range(2, len(triangle_list)+1):
        for j in range(len(triangle_list[-i])):
            triangle_list[-i][j] += max(triangle_list[-i+1][j], triangle_list[-i+1][j+1])
    return triangle_list[0][0]

#done in p21
def divisor_list(n: int, list_of_potential_primes: list = None) -> list:
    if n == 1:
        return [1]
    primeFactorList = prime_factors(n, list_of_potential_primes)
    return divisors_from_dict(primeFactorList)

def divisors_from_dict(dict_of_prime_factors: dict) -> list:
    divisors: list = [1]
    for prime in dict_of_prime_factors:
        new_divisors = []
        for divisor in divisors:
            for power in range(1, dict_of_prime_factors[prime] + 1):
                new_divisors.append(divisor * (prime ** power))
        divisors = divisors + new_divisors
    divisors.sort()
    return divisors

#done in p24
# def factorial(num: int) -> int:
#     fast_factorial = [1, 1, 2, 6, 24, 120]
#     if num <= 5:
#         return fast_factorial[num]
#     return num * factorial(num - 1)

#done in p24
#n starts at index 0
def find_nth_lexicographic_permutation(sorted_list: list, n: int) -> list:
    if len(sorted_list) == 1:
        return [sorted_list[0]]
    #big_factorial = factorial(len(sorted_list))
    big_factorial = math.factorial(len(sorted_list))
    if n >= big_factorial:
        return ["Error"]
    key_number = big_factorial // len(sorted_list)
    multiple = sorted_list.pop(n // key_number)
    remainder = n - ((n // key_number) * key_number)
    return [multiple] + find_nth_lexicographic_permutation(sorted_list, remainder)

# totient(m) * totient(n) = totient(m * n) if m and n are relatively prime
# Chinese Remainder Theorem
# Each prime power is relatively prime to each other so long as the primes are distinct
#
# On the totient of a prime power:
# Note that exactly p^k/p = p^(k-1) numbers will divide p
# So totient(p^k) = p^k - p^k/p = (p-1)/p p^k = (p-1) p^(k-1) = (1-1/p) p^k
# Multiplying all the primes will give totient(n) = n * (1-1/p_1) * (1-1/p_2)...
def totient(n: int, list_of_potential_primes: list = None) -> int:
    if n == 1:
        return 1
    totient = n
    prime_dicts = prime_factors(n, list_of_potential_primes)
    for prime in prime_dicts.keys():
        totient = (prime - 1) * totient // prime
    return totient