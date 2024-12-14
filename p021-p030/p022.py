def read_file_into_sorted_list_of_names(filename: str) -> list[str]:
    # open the file
    f = open(filename, "r")
    line = f.readline()
    f.close()
    arrayOfNames = line.split(",")
    for index in range(len(arrayOfNames)):
        arrayOfNames[index] = arrayOfNames[index].strip('"')
    # feeling lazy to sort it
    arrayOfNames.sort()
    return arrayOfNames


def p22solution1() -> int:
    arrayOfNames = read_file_into_sorted_list_of_names("p022Input.txt")
    total = 0
    nameNumber = 1
    for name in arrayOfNames:
        # when converted to hex, "A" becomes 65
        nameTotal = 0
        for char in name:
            nameTotal += ord(char) - 64
        total += nameNumber * nameTotal
        nameNumber += 1
    return total


if __name__ == "__main__":
    print(p22solution1())
