import copy

import miscHelperFunctions


# returns a list of lists where indexes...
# 0 is divisible by 5
# 012 is divisible by 11
# 123 is divisible by 13
# 234 is divisible by 17
def sub_string_divisibility_latter_half() -> list[list[int]]:
    list_of_potential_ints = []
    # the first number in the divisibility of 11 is either 5 or 0
    # if it is 0, then it is 0xx for some digit x, which is not pandigital.
    for d7d8 in range(100):
        if (500 + d7d8) % 11 == 0:
            for d9 in range(10):
                potential_list = [5, d7d8 // 10, d7d8 % 10]
                if (d7d8 * 10 + d9) % 13 == 0:
                    potential_list.append(d9)
                    for d10 in range(10):
                        if (potential_list[-2] * 100 + potential_list[-1] * 10 + d10) % 17 == 0:
                            potential_list.append(d10)
                            if miscHelperFunctions.is_pandigital(potential_list, True, 10):
                                list_of_potential_ints.append(potential_list)
                                break
    return list_of_potential_ints


def sub_string_divisibility() -> list[list[int]]:
    list_of_potential_ints = []
    list_of_potential_latter_half = sub_string_divisibility_latter_half()
    for potential_list in list_of_potential_latter_half:
        pandigital_digits_left_1 = [i for i in range(10)]
        for digit in potential_list:
            pandigital_digits_left_1.remove(digit)
        for d5 in pandigital_digits_left_1:
            if (d5 * 100 + potential_list[0] * 10 + potential_list[1]) % 7 == 0:
                pandigital_digits_left_2 = copy.deepcopy(pandigital_digits_left_1)
                pandigital_digits_left_2.remove(d5)
                new_potential_list = [d5] + potential_list
                for d3 in pandigital_digits_left_2:
                    for d4 in pandigital_digits_left_2:
                        if d3 != d4 and (d3 + d4 + d5) % 3 == 0 and d4 % 2 == 0:
                            pandigital_digits_left_3 = copy.deepcopy(pandigital_digits_left_2)
                            pandigital_digits_left_3.remove(d3)
                            pandigital_digits_left_3.remove(d4)
                            new_potential_list_2 = [d3, d4] + new_potential_list
                            list_of_potential_ints.append(
                                [pandigital_digits_left_3[0], pandigital_digits_left_3[1]] + new_potential_list_2)
                            list_of_potential_ints.append(
                                [pandigital_digits_left_3[1], pandigital_digits_left_3[0]] + new_potential_list_2)
    return list_of_potential_ints


# def sub_string_divisibility_check(check: list[int]) -> bool:
#     if not miscHelperFunctions.is_pandigital(check, False, 10):
#         return False
#     return ((check[1] * 100 + check[2] * 10 + check[3]) % 2 == 0 and
#             (check[2] * 100 + check[3] * 10 + check[4]) % 3 == 0 and
#             (check[3] * 100 + check[4] * 10 + check[5]) % 5 == 0 and
#             (check[4] * 100 + check[5] * 10 + check[6]) % 7 == 0 and
#             (check[5] * 100 + check[6] * 10 + check[7]) % 11 == 0 and
#             (check[6] * 100 + check[7] * 10 + check[8]) % 13 == 0 and
#             (check[7] * 100 + check[8] * 10 + check[9]) % 17 == 0)

def p43solution1() -> int:
    list_of_ints = sub_string_divisibility()
    sum1 = 0
    for integer_list in list_of_ints:
        if integer_list[0] != 0:
            integer_string = ""
            for char in integer_list:
                integer_string += str(char)
            sum1 += int(integer_string)
    return sum1


if __name__ == "__main__":
    print(p43solution1())
