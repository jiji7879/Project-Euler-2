def champernowne_constant_digit(n: int) -> int:
    if n <= 0:
        return -1
    if n < 10:
        return n

    # get to the same 10 ** n
    currentDigit = 9
    digit_length = 2
    while currentDigit + digit_length * 9 * 10 ** (digit_length - 1) < n:
        currentDigit += digit_length * 9 * 10 ** (digit_length - 1)
        digit_length += 1

    # get to the correct number
    currentDigit += 1
    startingNumber = 10 ** (digit_length - 1)
    startingNumber += (n - currentDigit) // digit_length
    currentDigit += (n - currentDigit) // digit_length * digit_length

    return int(str(startingNumber)[n-currentDigit])

def p40solution1() -> int:
    product = 1
    for i in range(7):
        product *= champernowne_constant_digit(10 ** i)
    return product

if __name__ == "__main__":
    p40solution1()