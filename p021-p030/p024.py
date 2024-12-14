import miscHelperFunctions


def p24solution1() -> int:
    permutation = miscHelperFunctions.find_nth_lexicographic_permutation(list(range(10)), 1000000 - 1)
    string = ""
    for char in permutation:
        string += str(char)
    return int(string)


if __name__ == "__main__":
    print(p24solution1())
