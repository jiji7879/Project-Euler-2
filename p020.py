import helperFunctions

def big_factorial(num: int) -> list:
    factorial_list = [1]
    for i in range(2, num+1):
        num_list = [int(j) for j in str(i)]
        factorial_list = helperFunctions.big_number_multiplication(factorial_list, num_list)
    return factorial_list

def p20solution1(num: int) -> int:
    factorial_list = big_factorial(num)
    return sum(factorial_list)

if __name__ == "__main__":
    print(p20solution1(100))