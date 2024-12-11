import primeHelperFunctions

def p027_potential_primes(n: int) -> list:
    max_num = n ** 2 + 1000 * n + 1000
    return primeHelperFunctions.primes_until_n(max_num)

def find_max_consec_primes(a: int, b: int, max_num: int, list_of_potential_primes: list) -> int:
    n = 0
    while n < max_num:
        if (n ** 2 + a * n + b) not in list_of_potential_primes:
            return n
        n += 1
    return n

def p27solution1() -> int:
    # check 100 first
    max_solutions_list = []
    max_solution = 0
    max_a = -1000
    max_b = -1000

    # the polynomial at n = 0 being prime is equivalent to b to being prime.
    b_primes = primeHelperFunctions.primes_until_n(1000)

    #test 100 first
    potential_list_of_primes = p027_potential_primes(100)
    for b in b_primes:
        # For n = 1 to be prime, we note that 1 + a + b >= 2, so a >= 2 - b - 1
        for a in range(min(-999, 2-b-1), 1000):
            consec_primes = find_max_consec_primes(a, b, 100, potential_list_of_primes)
            if consec_primes == 100:
                max_solutions_list.append((a, b))
            elif consec_primes > max_solution:
                max_solution = consec_primes
                max_a = a
                max_b = b

    if len(max_solutions_list) == 0:
        return max_a * max_b
    elif len(max_solutions_list) == 1:
        return max_solutions_list[0][0] * max_solutions_list[0][1]

    #this will terminate eventually, given that n = a * b will always give a non-prime
    max_n = 200
    while True:
        new_solutions_list = []
        potential_list_of_primes = p027_potential_primes(max_n)
        for potential in max_solutions_list:
            consec_primes = find_max_consec_primes(potential[0], potential[1], max_n, potential_list_of_primes)
            if consec_primes == max_n:
                new_solutions_list.append((potential[0], potential[1]))
            elif consec_primes > max_solution:
                max_solution = consec_primes
                max_a = potential[0]
                max_b = potential[1]

        max_solutions_list = new_solutions_list
        if len(max_solutions_list) == 0:
            return max_a * max_b
        elif len(max_solutions_list) == 1:
            return max_solutions_list[0][0] * max_solutions_list[0][1]

        max_n += 100

if __name__ == "__main__":
    print(p27solution1())