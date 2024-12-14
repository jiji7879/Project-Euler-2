def collatz_sequence(starting_int: int) -> list[int]:
    sequence = [starting_int]
    # we assume that it does end at 1
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    return sequence


def starting_collatz_sequences(max_num: int) -> dict[int, int]:
    dict_of_sequences = {}
    for i in range(max_num):
        if max_num - i not in dict_of_sequences:
            sequence = collatz_sequence(max_num - i)
            sequence_length = len(sequence)
            for index in range(sequence_length):
                if sequence[index] not in dict_of_sequences:
                    dict_of_sequences[sequence[index]] = sequence_length - index
                else:
                    break
    return dict_of_sequences


def p14solution1(max_num: int) -> int:
    collatz_lengths = starting_collatz_sequences(max_num)
    max_sequence = 0
    max_key = 0

    # assuming unique solution
    for key, value in collatz_lengths.items():
        if value > max_sequence and key < max_num:
            max_sequence = value
            max_key = key
    return max_key


if __name__ == "__main__":
    print(p14solution1(1000000))
