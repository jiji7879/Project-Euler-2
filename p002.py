def sum_even_fibonacci(limit: int) -> int:
    sum1=2
    fibonacci = [1,2]
    while fibonacci[-1] < limit:
        fibonacci = [fibonacci[1], fibonacci[0]+fibonacci[1]]
        if fibonacci[1] % 2 == 0:
            sum1 += fibonacci[1]
    return sum1

def p2solution1() -> int:
    return sum_even_fibonacci(4000000)

if __name__ == "__main__":
    print(p2solution1())