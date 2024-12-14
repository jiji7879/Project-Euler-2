def p4solution1() -> int:
    listOfPalindromes = []
    for i in range(100, 1000):
        for j in range(i, 1000):
            if str(i * j) == str(i * j)[::-1]:
                listOfPalindromes.append(i * j)
    return max(listOfPalindromes)


if __name__ == "__main__":
    print(p4solution1())
