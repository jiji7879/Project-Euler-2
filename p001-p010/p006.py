def sum_of_squares(max_num: int) -> int:
    sum1 = 0
    for i in range(1, max_num + 1):
        sum1 += i ** 2
    return sum1


def square_of_sum(max_num: int) -> int:
    sum1 = 0
    for i in range(1, max_num + 1):
        sum1 += i
    return sum1 ** 2


def p6solution1() -> int:
    return square_of_sum(100) - sum_of_squares(100)


if __name__ == "__main__":
    print(p6solution1())
