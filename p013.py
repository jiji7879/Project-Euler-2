def read_file_as_one_number(filename: str) -> list:
    # open the file
    f = open(filename, "r")

    arrayOfNumbers = []
    #read each line
    for line in f:
        #we're doing the first 14 characters because of an arbitrary suggestion
        arrayOfNumbers.append(int(line[0:14]))
    return arrayOfNumbers

def p13solution1() -> str:
    x = read_file_as_one_number("p13.txt")
    y = 0
    for i in range(len(x)):
        y += x[i]

    #return the first 10 digits of the sum
    return str(y)[0:10]

if __name__ == "__main__":
    print(p13solution1())