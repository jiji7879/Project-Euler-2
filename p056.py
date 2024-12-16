import miscHelperFunctions


def p56solution1():
    max_digit_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            a_b_digit_sum = miscHelperFunctions.digit_sum(a ** b)
            if a_b_digit_sum > max_digit_sum:
                max_digit_sum = a_b_digit_sum
    return max_digit_sum


if __name__ == "__main__":
    print(p56solution1())
