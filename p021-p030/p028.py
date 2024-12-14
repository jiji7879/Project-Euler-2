def find_sum_of_diagonals(size: int) -> int:
    if size % 2 == 0:
        return 0
    if size == 1:
        return 1
    total = 1
    i = 1
    diff = 2
    for j in range(3, size + 1, 2):
        for _ in range(4):
            i += diff
            total += i
        diff += 2
    return total


if __name__ == "__main__":
    print(findSumOfDiagonals(1001))
