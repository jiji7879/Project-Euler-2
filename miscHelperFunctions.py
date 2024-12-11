import math

#done in p11
def read_file_as_array_of_numbers(filename: str) -> list:
    # open the file
    f = open(filename, "r")

    arrayOfNumbers = []
    #read each line
    for line in f:
        arrayOfNumbersInLine = []
        #split the line into an array of numbers
        for number in line.split():
            # put it in as a number
            arrayOfNumbersInLine.append(int(number))
        arrayOfNumbers.append(arrayOfNumbersInLine)
    return arrayOfNumbers

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
    for i in range(2, len(triangle_list)+1):
        for j in range(len(triangle_list[-i])):
            triangle_list[-i][j] += max(triangle_list[-i+1][j], triangle_list[-i+1][j+1])
    return triangle_list[0][0]


#done in p24
# def factorial(num: int) -> int:
#     fast_factorial = [1, 1, 2, 6, 24, 120]
#     if num <= 5:
#         return fast_factorial[num]
#     return num * factorial(num - 1)

#done in p24
#n starts at index 0
def find_nth_lexicographic_permutation(sorted_list: list, n: int) -> list:
    if len(sorted_list) == 1:
        return [sorted_list[0]]
    #big_factorial = factorial(len(sorted_list))
    big_factorial = math.factorial(len(sorted_list))
    if n >= big_factorial:
        return ["Error"]
    key_number = big_factorial // len(sorted_list)
    multiple = sorted_list.pop(n // key_number)
    remainder = n - ((n // key_number) * key_number)
    return [multiple] + find_nth_lexicographic_permutation(sorted_list, remainder)