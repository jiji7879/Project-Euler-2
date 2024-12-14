import primeHelperFunctions


def circular_primes(max_number: int) -> list[int]:
    if max_number < 1:
        return []
    elif max_number <= 2:
        return [2]
    elif max_number <= 4:
        return [2, 3]
    elif max_number <= 5:
        return [2, 3, 5]
    list_of_circular_primes = [2, 5]
    primes = primeHelperFunctions.primes_until_n(max_number)
    for test_number in primes:
        test_number_list = [i for i in str(test_number)]
        if '2' in test_number_list or '4' in test_number_list or '6' in test_number_list or '8' in test_number_list or '0' in test_number_list or '5' in test_number_list:
            continue
        has_non_prime = False
        index = 1
        while not has_non_prime and index < len(test_number_list):
            test_thing = test_number_list.pop()
            test_number_list.insert(0, test_thing)
            test_number_string = ""
            for char in test_number_list:
                test_number_string += str(char)
            if int(test_number_string) not in primes:
                has_non_prime = True
            index += 1
        if not has_non_prime:
            list_of_circular_primes.append(test_number)
    return list_of_circular_primes


def p35solution1(max_num: int) -> int:
    return len(circular_primes(max_num))


if __name__ == "__main__":
    print(p35solution1(1000000))
