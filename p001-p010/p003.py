def find_factor_of_number(number: int, divisor_start: int = 2) -> int:
    if divisor_start == 1:
        divisor_start = 2
    for i in range(divisor_start, int((number ** 0.5) // 1) + 1):
        if number % i == 0:
            return i
    return -1


def find_biggest_factor(number: int) -> int:
    factor = 1
    while factor != -1:
        number = number // factor
        factor = find_factor_of_number(number, factor)
    return number


def p3solution1() -> int:
    return find_biggest_factor(600851475143)


if __name__ == "__main__":
    print(p3solution1())
