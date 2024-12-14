import miscHelperFunctions


def p11solution1() -> int:
    array = miscHelperFunctions.read_file_as_array_of_numbers("p011.txt")
    maxProduct = 0

    numRows = len(array)
    numColumns = len(array[0])

    # horizontal
    for i in range(numRows):
        for j in range(numColumns - 3):
            product = 1
            for k in range(0, 4):
                product *= array[i][j + k]
            if product > maxProduct:
                maxProduct = product

    # vertical
    for i in range(numColumns):
        for j in range(numRows - 3):
            product = 1
            for k in range(0, 4):
                product *= array[j + k][i]
            if product > maxProduct:
                maxProduct = product

    # diagonal-right
    for i in range(numRows - 3):
        for j in range(numColumns - 3):
            product = 1
            for k in range(0, 4):
                product *= array[i + k][j + k]
            if product > maxProduct:
                maxProduct = product

    # diagonal-left
    for i in range(3, numRows):
        for j in range(numColumns - 3):
            product = 1
            for k in range(0, 4):
                product *= array[i - k][j + k]
            if product > maxProduct:
                maxProduct = product
    return maxProduct


def p11solution2() -> int:
    # by fucking eyes
    return 70600674

if __name__ == "__main__":
    print(p11solution1())