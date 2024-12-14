def find_reciprocal_cycle_length(n: int) -> int:
    if n <= 0:
        return -1
    remainder = 1
    dict_of_reciprocals = {}
    division_index = 1

    # this should terminate by cycle n+1 since dict_of_reciprocals should only have numbers modulo n.
    while division_index < n+3:
        remainder *= 10
        remainder = remainder % n
        if remainder == 0:
            return 0
        if remainder in dict_of_reciprocals:
            return division_index - dict_of_reciprocals[remainder]
        else:
            dict_of_reciprocals[remainder] = division_index
        division_index += 1
    return -1

def p26solution1():
    max_cycle = 0
    max_index = 0
    for i in range(1000):
        result = find_reciprocal_cycle_length(i)
        if result > max_cycle:
            max_cycle = result
            max_index = i
    return max_index

if __name__ == "__main__":
    print(p26solution1())