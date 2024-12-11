import helperFunctions

def p21solution(max_num: int) -> int:
    divisorSums = {}
    sum1 = 0
    for i in range(1, max_num+1):
        divisor_sum = sum(helperFunctions.divisor_list(i)) - i
        divisorSums[i] = divisor_sum
        if i != divisor_sum and divisor_sum in divisorSums and divisorSums[divisor_sum] == i:
            print(divisor_sum, i)
            if divisor_sum < 10000:
                sum1 += divisor_sum
            sum1 += i
    return sum1

if __name__ == "__main__":
    print(p21solution(10000))