ONES_LIST = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#ones_length = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]
ONE_TEN_LIST = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS_LIST = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED_STRING = "hundred"
THOUSAND_STRING = "thousand"
AND_STRING = "and"

def create_english_string(num: int) -> str:
    if num < 0 or num > 1000:
        return "Not implemented"
    elif num == 0:
        return ONES_LIST[0]

    string = ""
    if num >= 1000:
        string += ONES_LIST[num // 1000]
        string += f" {THOUSAND_STRING}"
    num = num % 1000
    if num >= 100:
        if string != "":
            string += " "
        string += ONES_LIST[num // 100]
        string += f" {HUNDRED_STRING}"
    num = num % 100
    if string != "" and num != 0:
        string += f" {AND_STRING} "
    if 10 <= num < 20:
        string += ONE_TEN_LIST[num % 10]
        return string
    if num >= 20:
        string += TENS_LIST[num // 10]
        if num % 10 != 0:
            string += " "
    if num % 10 != 0:
        string += ONES_LIST[num % 10]
    return string

def english_string_length(num: int) -> int:
    if num < 0 or num > 1000:
        return 0
    elif num == 0:
        return len(ONES_LIST[0])

    string_count = 0
    if num >= 1000:
        string_count += len(ONES_LIST[num // 1000])
        string_count += len(THOUSAND_STRING)
    num = num % 1000
    if num >= 100:
        string_count += len(ONES_LIST[num // 100])
        string_count += len(HUNDRED_STRING)
    num = num % 100
    if string_count != 0 and num != 0:
        string_count += len(AND_STRING)
    if 10 <= num < 20:
        string_count += len(ONE_TEN_LIST[num % 10])
        return string_count
    if num >= 20:
        string_count += len(TENS_LIST[num // 10])
    if num % 10 != 0:
        string_count += len(ONES_LIST[num % 10])
    return string_count

def p17solution(max_num: int) -> int:
    total = 0
    for i in range(1, max_num+1):
        total += english_string_length(i)
    return total

if __name__ == "__main__":
    print(p17solution(1000))
