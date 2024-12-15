import bigNumberHelperFunctions


# last 10 digits
def big_sum_of_self_powers(max_num: int, num_of_digits: int) -> list[int]:
    sum_of_self_powers = [0 for _ in range(num_of_digits)]
    for i in range(1, max_num + 1):
        i_power = [i]
        for j in range(2, i + 1):
            i_power = bigNumberHelperFunctions.big_number_multiplication(i_power, [i])
            if len(i_power) > num_of_digits:
                i_power = i_power[-num_of_digits:]
        sum_of_self_powers = bigNumberHelperFunctions.big_number_addition(sum_of_self_powers, i_power)
        if len(sum_of_self_powers) > num_of_digits:
            sum_of_self_powers = sum_of_self_powers[-num_of_digits:]
    return sum_of_self_powers


if __name__ == "__main__":
    print(big_sum_of_self_powers(1000, 10))
