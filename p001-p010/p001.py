# solution 1: The quick and easy way
def p1solution1(n: int) -> int:
    sum1 = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum1 += i
    return sum1


# solution 2: Generalized. Slower for now, but will be better in next solution
def slow_sum_of_multiples(multiple: int, limit: int) -> int:
    sum1 = 0
    for i in range(limit):
        if i % multiple == 0:
            sum1 += i
    return sum1


# sum up multiples of 3 and 5. We will double count multiples of 15, so take those out.
def p1solution2(n: int) -> int:
    return slow_sum_of_multiples(3, n) + slow_sum_of_multiples(5, n) - slow_sum_of_multiples(15, n)


# solution 3: Optimize sum of multiples function via Gauss summation trick
def sum_of_multiples(multiple: int, limit: int) -> int:
    highestMultiple = (limit - 1) // multiple
    return multiple * (highestMultiple * (highestMultiple + 1)) // 2


def p1solution3(n: int) -> int:
    return sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n)


# solution 4: We already have the limit of 1000.
def p1solution4() -> int:
    return 3 * (333 * 334) // 2 + 5 * (199 * 200) // 2 - 15 * (66 * 67) // 2


if __name__ == "__main__":
    print(p1solution4())
