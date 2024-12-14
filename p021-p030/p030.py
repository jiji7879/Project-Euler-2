#Note that 10^5 = 100,000
# So 6 * 10^5 = 600,000 and thus 6 * 9^5 < 600,000 and is a maximum.

def sum_of_fifth_powers() -> list:
    list_of_fifth_power_number_sums = []
    for i in range(10, 999999):
        total = 0
        for char in str(i):
            total += int(char) ** 5
        if total == i:
            list_of_fifth_power_number_sums.append(i)
    return list_of_fifth_power_number_sums

def p30solution1():
    fifth_power_list = sum_of_fifth_powers()
    return sum(fifth_power_list)

if __name__ == "__main__":
    print(p30solution1())