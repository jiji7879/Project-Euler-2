import miscHelperFunctions

def p67solution1(filename: str) -> int:
    triangle_list = miscHelperFunctions.read_file_as_array_of_numbers(filename)
    #hoping that the input is done correctly
    return miscHelperFunctions.path_sum(triangle_list)

if __name__ == "__main__":
    print(p67solution1("p067Input.txt"))