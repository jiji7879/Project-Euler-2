import helperFunctions

def p7solution1() -> int:
    return helperFunctions.first_n_primes(10001)[10000]

if __name__ == "__main__":
    print(p7solution1())