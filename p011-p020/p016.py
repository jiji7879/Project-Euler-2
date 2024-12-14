import bigNumberHelperFunctions

def p16solution1() -> int:
    # Although the length of this is 302, Python seems to have the number on lock.
    # print(len(str(2**1000))) # 302
    return helperFunctions.digit_sum(2**1000)

def p16solution2() -> int:
    # Suppose we do not have the luxury of 302-length integers.
    power_125 = 2**125
    #print(len(str(power_125))) # 38
    power_125_list = [int(i) for i in str(power_125)]
    power_250_list = bigNumberHelperFunctions.big_number_multiplication(power_125_list, power_125_list)
    power_500_list = bigNumberHelperFunctions.big_number_multiplication(power_250_list, power_250_list)
    power_1000_list = bigNumberHelperFunctions.big_number_multiplication(power_500_list, power_500_list)
    return sum(power_1000_list)

if __name__ == "__main__":
    print(p16solution1())
    print(p16solution2())