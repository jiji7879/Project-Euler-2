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
def multiply_prime_factors(dict_of_prime_factors1: dict, dict_of_prime_factors2: dict):
    for prime in dict_of_prime_factors1:
        if prime in dict_of_prime_factors2:
            dict_of_prime_factors2[prime]= dict_of_prime_factors2[prime] + dict_of_prime_factors1[prime]
        else:
            dict_of_prime_factors2[prime]=dict_of_prime_factors1[prime]
    return dict_of_prime_factors2
