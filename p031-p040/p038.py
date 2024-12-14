import miscHelperFunctions


# note that the rules state we can't have just 123456789 * 1 = 123456789
# and 10000 * 2 = 20000, which is 10 digits long
# so we can only go up to 4 digits.
# more importantly, we can only multiply up to 9//len(a).
def largest_pandigital_multiple() -> int:
    largest_pandigital = 0
    for a in range(1, 9999):
        if int(str(a)[0]) < int(str(largest_pandigital)[0]):
            continue
        pandigital_list = []
        pandigital_length = 0
        for b in range(1, 9):
            pandigital_list.append(a * b)
            pandigital_length += len(str(a * b))
            if pandigital_length > 9:
                break
            elif pandigital_length == 9:
                if miscHelperFunctions.is_pandigital(pandigital_list, False):
                    pandigital_string = ""
                    for number in pandigital_list:
                        pandigital_string += str(number)
                    if int(pandigital_string) > largest_pandigital:
                        largest_pandigital = int(pandigital_string)
                break
            elif not miscHelperFunctions.is_pandigital(pandigital_list, True):
                break
    return largest_pandigital


if __name__ == "__main__":
    print(largest_pandigital_multiple())
