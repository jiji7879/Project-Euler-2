import helperFunctions
from helperFunctions import primes_until_n


def list_of_abundant_numbers(max_num: int) -> list:
    abundant_numbers = []
    primes = primes_until_n(max_num)
    for i in range(1, max_num+1):
        if sum(helperFunctions.divisor_list(i, primes)) > 2 * i:
            abundant_numbers.append(i)
    return abundant_numbers

def sum_until_n(n: int):
    return n * (n+1) // 2

def p23solution1() -> list:
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