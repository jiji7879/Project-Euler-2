from collections import defaultdict


def p092solution1(max_num: int) -> int:
    dict_of_square_digit_shortcuts = defaultdict(int)
    dict_of_square_digit_shortcuts[1] = 1
    dict_of_square_digit_shortcuts[89] = 89
    end_1 = 0
    end_89 = 0
    for i in range(1, max_num + 1)[::-1]:
        if i in dict_of_square_digit_shortcuts:
            if dict_of_square_digit_shortcuts[i] == 1:
                end_1 += 1
            else:
                end_89 += 1
            continue
        digit_chain_list = [i]
        while digit_chain_list[-1] not in dict_of_square_digit_shortcuts:
            square_digit_sum = 0
            for digit in list(str(digit_chain_list[-1])):
                square_digit_sum += int(digit) * int(digit)
            digit_chain_list.append(square_digit_sum)
        end_number = dict_of_square_digit_shortcuts[digit_chain_list[-1]]
        for item in digit_chain_list:
            dict_of_square_digit_shortcuts[item] = end_number
        if end_number == 1:
            end_1 += 1
        else:
            end_89 += 1
    return end_89


if __name__ == "__main__":
    print(p092solution1(9999999))
