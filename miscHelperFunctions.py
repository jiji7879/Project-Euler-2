import math


# done in p11
def read_file_as_array_of_numbers(filename: str) -> list[list[int]]:
    # open the file
    f = open(filename, "r")

    arrayOfNumbers = []
    # read each line
    for line in f:
        arrayOfNumbersInLine = []
        # split the line into an array of numbers
        for number in line.split():
            # put it in as a number
            arrayOfNumbersInLine.append(int(number))
        arrayOfNumbers.append(arrayOfNumbersInLine)
    return arrayOfNumbers


# done in p22
def read_file_into_sorted_list_of_names(filename: str) -> list[str]:
    # open the file
    f = open(filename, "r")
    line = f.readline()
    f.close()
    arrayOfNames = line.split(",")
    for index in range(len(arrayOfNames)):
        arrayOfNames[index] = arrayOfNames[index].strip('"')
    # feeling lazy to sort it
    arrayOfNames.sort()
    return arrayOfNames


# done in p16
def digit_sum(num: int) -> int:
    num_string = str(num)
    digit_sum1 = 0
    for char in num_string:
        digit_sum1 += int(char)
    return digit_sum1


# done in p18, at least reused in p67
# the triangle_list assumes a list of ascending lengths increasing by exactly 1
# for example, the list from the p18 sample input should be [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
def path_sum(triangle_list: list) -> int:
    for i in range(2, len(triangle_list) + 1):
        for j in range(len(triangle_list[-i])):
            triangle_list[-i][j] += max(triangle_list[-i + 1][j], triangle_list[-i + 1][j + 1])
    return triangle_list[0][0]


# done in p24
# def factorial(num: int) -> int:
#     fast_factorial = [1, 1, 2, 6, 24, 120]
#     if num <= 5:
#         return fast_factorial[num]
#     return num * factorial(num - 1)

# done in p24
# n starts at index 0
def find_nth_lexicographic_permutation(sorted_list: list, n: int) -> list:
    if len(sorted_list) == 1:
        return [sorted_list[0]]
    # big_factorial = factorial(len(sorted_list))
    big_factorial = math.factorial(len(sorted_list))
    if n >= big_factorial:
        return ["Error"]
    key_number = big_factorial // len(sorted_list)
    multiple = sorted_list.pop(n // key_number)
    remainder = n - ((n // key_number) * key_number)
    return [multiple] + find_nth_lexicographic_permutation(sorted_list, remainder)


def is_pandigital(list_to_check: list[int], partial: bool, max_int: int = 9) -> bool:
    if max_int < 1 or max_int > 10:
        return False
    if max_int == 10:
        pandigital_digit_set = {i for i in range(max_int + 1)}
    else:
        pandigital_digit_set = {i for i in range(1, max_int + 1)}
    list_digit_set = set()
    for item in list_to_check:
        for char in str(item):
            if int(char) in list_digit_set:
                return False
            list_digit_set.add(int(char))
    if partial:
        return True if list_digit_set.issubset(pandigital_digit_set) else False
    else:
        return True if list_digit_set == pandigital_digit_set else False


def text_to_number(char: str) -> int:
    # ord(A) = 65, ord(Z) = 90
    if 65 <= ord(char) <= 90:
        return ord(char) - 64

    # ord(a) = 97, ord(z) = 122
    if 97 <= ord(char) <= 122:
        return ord(char) - 96

    return 0
