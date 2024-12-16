import bigNumberHelperFunctions


def last_ten_digits_of_large_mersenne_prime() -> list:
    digit_list = [2]
    # since 7830456 is divisible by 4, we can multiply by 2 ** 4 to make it faster
    for _ in range(7830456 // 4):
        digit_list = bigNumberHelperFunctions.big_number_multiplication(digit_list, [1, 6])
        if len(digit_list) > 10:
            digit_list = digit_list[-10:]
    digit_list = bigNumberHelperFunctions.big_number_multiplication(digit_list, [2, 8, 4, 3, 3])
    if len(digit_list) > 10:
        digit_list = digit_list[-10:]
    digit_list = bigNumberHelperFunctions.big_number_addition(digit_list, [1])
    return digit_list


if __name__ == "__main__":
    mersenne_string = ""
    for digit in last_ten_digits_of_large_mersenne_prime():
        mersenne_string += str(digit)
    print(int(mersenne_string))
