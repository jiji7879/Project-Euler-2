# done in p15
# the polynomial list is structured from highest order to least
# for example, multiplying (x^2+1)(x^3-2x^2+x-1) correlates to [1,0,1] and [1,-2,1,-1]
def polynomial_multiplication(polynomial1: list, polynomial2: list) -> list:
    multiplication_result = [0 for _ in range(len(polynomial1)+len(polynomial2)-1)]
    for polynomial_2_term_index in range(len(polynomial2)):
        for polynomial_1_term_index in range(len(polynomial1)):
            multiplication_result[polynomial_1_term_index+polynomial_2_term_index] += (
                    polynomial1[polynomial_1_term_index] * polynomial2[polynomial_2_term_index])
    return multiplication_result

# done in p16
def big_number_multiplication(big_num1: list, big_num2: list, base: int = 10) -> list:
    multiplication_result = polynomial_multiplication(big_num1, big_num2)
    return big_number_carrying(multiplication_result, base)

# done in p25
def big_number_addition(big_num1: list, big_num2: list, base: int = 10) -> list:
    if len(big_num1) > len(big_num2):
        big_num2 = [0 for _ in range(len(big_num1)-len(big_num2))] + big_num2
    else:
        big_num1 = [0 for _ in range(len(big_num2) - len(big_num1))] + big_num1
    addition_result = [0 for _ in range(len(big_num1))]
    for i in range(len(big_num1)):
        addition_result[i] = big_num1[i] + big_num2[i]
    return big_number_carrying(addition_result, base)

def big_number_carrying(big_num_list: list, base: int) -> list:
    for negative_index in range(1, len(big_num_list)):
        if big_num_list[-negative_index] >= base:
            big_num_list[-negative_index - 1] += big_num_list[-negative_index] // base
            big_num_list[-negative_index] = big_num_list[-negative_index] % base
    while big_num_list[0] >= base:
        big_num_list.insert(0, big_num_list[0] // base)
        # the rest of the result should be pushed to the right by 1
        big_num_list[1] = big_num_list[1] % base
    return big_num_list
