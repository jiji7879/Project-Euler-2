import miscHelperFunctions


def p22solution1() -> int:
    arrayOfNames = miscHelperFunctions.read_file_into_sorted_list_of_names("p022Input.txt")
    total = 0
    nameNumber = 1
    for name in arrayOfNames:
        # when converted to hex, "A" becomes 65
        nameTotal = 0
        for char in name:
            nameTotal += miscHelperFunctions.text_to_number(char)
        total += nameNumber * nameTotal
        nameNumber += 1
    return total


if __name__ == "__main__":
    print(p22solution1())
