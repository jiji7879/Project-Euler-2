import primeHelperFunctions


def list_of_abundant_numbers(max_num: int) -> list[int]:
    abundant_numbers = []
    primes = primeHelperFunctions.primes_until_n(max_num)
    for i in range(1, max_num + 1):
        if sum(primeHelperFunctions.divisor_list(i, primes)) > 2 * i:
            abundant_numbers.append(i)
    return abundant_numbers


def sum_until_n(n: int) -> int:
    return n * (n + 1) // 2


def p23solution1() -> int:
    abundant_numbers = list_of_abundant_numbers(28123)
    sum_of_two_abundant = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if abundant_numbers[i] + abundant_numbers[j] <= 28123:
                sum_of_two_abundant.add(abundant_numbers[i] + abundant_numbers[j])
    sum_of_abundant_sums = 0
    for i in sum_of_two_abundant:
        sum_of_abundant_sums += i
    return sum_until_n(28123) - sum_of_abundant_sums


if __name__ == "__main__":
    print(p23solution1())
