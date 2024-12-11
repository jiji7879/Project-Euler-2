def read_file_as_one_number(filename: str) -> list:
    # open the file
    f = open(filename, "r")

    arrayOfNumbers = []
    #read each line
    for line in f:
        #don't forget to delete the newline at the end of each line
        for char in line.rstrip():
            # put it in as a number
            arrayOfNumbers.append(int(char))
    return arrayOfNumbers

def p8solution1() -> int:
    array = read_file_as_one_number("p008.txt")
    i=0
    maxProduct = 0
    while i+12 <= len(array):
        product = 1
        for j in range(0,13):
            product *= array[i+j]
            if array[i+j] == 0:
                break
        if product > maxProduct:
            maxProduct = product
        i+=1
    return maxProduct

def p8solution2():
    # by literally eyes
    return 23514624000

if __name__ == "__main__":
    print(p8solution1())