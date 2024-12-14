def p5solution1() -> int:
    flag = False
    number = 2520
    while not flag:
        i = 11
        print(number)
        while number % i == 0:
            i = i + 1
            if i == 21:
                flag = True
        number += 2520
    return number - 2520


def p5solution2() -> int:
    # Get all the prime factors from 1-20 and take the union/maximum
    return 2 ** 4 * 3 ** 2 * 5 * 7 * 11 * 13 * 17 * 19


if __name__ == "__main__":
    print(p5solution2())
