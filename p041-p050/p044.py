def add_pentagonal_number(pentagonal_list: list) -> list:
    if len(pentagonal_list) == 0:
        return [1]
    return pentagonal_list + [(len(pentagonal_list) + 1) * (3 * (len(pentagonal_list) + 1) - 1) // 2]


# y = x(3x-1)/2
# 2y = 3x^2 - x
# 0 = 3x^2 - x - 2y
# x = (1 pm sqrt(1+24y))/6
# 6x - 1 = sqrt(1+24y)
def is_pentagonal(num: int) -> bool:
    square_root = (1 + 24 * num) ** 0.5
    if square_root == int(square_root) and int(square_root) % 6 == 5:
        return True


def find_a_pentagonal_sum_and_difference() -> (int, int, list):
    pentagonal_list = [1, 5]
    right_index = 1
    save_solution = (0, 0, [])
    while save_solution == (0, 0, []):
        for left_index in range(right_index):
            if pentagonal_list[right_index] - pentagonal_list[left_index] in pentagonal_list:
                pentagonal_sum = pentagonal_list[left_index] + pentagonal_list[right_index]
                if is_pentagonal(pentagonal_sum):
                    save_solution = (left_index, right_index, pentagonal_list)
        if len(pentagonal_list) <= right_index + 1:
            pentagonal_list = add_pentagonal_number(pentagonal_list)
        right_index += 1
    return save_solution


def find_minimal_pentagonal_sum_and_difference() -> (int, int, list):
    pentagonal_left, pentagonal_right, pentagonal_list = find_a_pentagonal_sum_and_difference()
    min_diff = pentagonal_list[pentagonal_right] - pentagonal_list[pentagonal_left]
    print(f"One solution found: {min_diff}")  # it turns out that this is the solution
    right_index = pentagonal_right
    while right_index < len(pentagonal_list):
        if pentagonal_list[right_index] - pentagonal_list[right_index - 1] > min_diff:
            break
        if right_index == len(pentagonal_list) - 1 and pentagonal_list[-1] - pentagonal_list[-2] < min_diff:
            pentagonal_list = add_pentagonal_number(pentagonal_list)
        for left_index in range(right_index):
            if pentagonal_list[right_index] - pentagonal_list[left_index] >= min_diff:
                continue
            if pentagonal_list[right_index] - pentagonal_list[left_index] in pentagonal_list:
                pentagonal_sum = pentagonal_list[left_index] + pentagonal_list[right_index]
                if is_pentagonal(pentagonal_sum):
                    min_diff = pentagonal_list[right_index] - pentagonal_list[left_index]
                    print(f"New min diff: {min_diff}")
                    continue
    return min_diff


if __name__ == "__main__":
    print(find_minimal_pentagonal_sum_and_difference())
