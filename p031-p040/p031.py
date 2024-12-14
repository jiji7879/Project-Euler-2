def find_number_of_partitions(num: int, possible_partitions: list[int]) -> int:
    if num < 0 or len(possible_partitions) == 0:
        return 0
    elif num == 0:
        return 1
    elif len(possible_partitions) == 1:
        return 1 if num % possible_partitions[0] == 0 else 0

    number_of_partitions = 0
    num_minus_partition = num
    while num_minus_partition >= 0:
        number_of_partitions += find_number_of_partitions(num_minus_partition, possible_partitions[1:])
        num_minus_partition = num_minus_partition - possible_partitions[0]
    return number_of_partitions


# check 10 for 10, 5, 2, 1
# 10, 5-5, 5-2-2-1, 5-2-1-1-1, 5-1-1-1-1, 2-2-2-2-2, 2-2-2-2-1-1, +4
# 11 partitions
def p31solution1() -> int:
    return find_number_of_partitions(200, [1, 2, 5, 10, 20, 50, 100, 200])


if __name__ == "__main__":
    print(p31solution1())
