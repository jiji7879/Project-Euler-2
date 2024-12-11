import helperFunctions

def p18solution1(filename: str) -> int:
    triangle_list = helperFunctions.read_file_as_array_of_numbers(filename)
    #hoping that the input is done correctly
    return helperFunctions.path_sum(triangle_list)

if __name__ == "__main__":
    print(p18solution1("p018SampleInput1.txt"))
    print(p18solution1("p018Input.txt"))