import miscHelperFunctions


def p42solution1() -> int:
    list_of_names = miscHelperFunctions.read_file_into_sorted_list_of_names("p042Input.txt")
    # 1/2 (1)(2) = 1
    triangle_number_list = [1]
    total_score = 0
    for name in list_of_names:
        score = 0
        for char in name:
            score += miscHelperFunctions.text_to_number(char)
        while score >= triangle_number_list[-1]:
            triangle_number_list.append((len(triangle_number_list) + 1) * (len(triangle_number_list) + 2) // 2)
        if score in triangle_number_list:
            total_score += 1
    return total_score


if __name__ == "__main__":
    print(p42solution1())
