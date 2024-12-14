def decimal_binary_palindromes(max_num: int) -> list:
    palindrome_list = []
    for i in range(1, max_num+1):
        if str(i) == str(i)[::-1]:
            binary = bin(i)[2:]
            if binary == binary[::-1]:
                palindrome_list.append(i)
    return palindrome_list

def p36solution1(max_num: int) -> int:
    palindromes = decimal_binary_palindromes(max_num)
    return sum(palindromes)

if __name__ == "__main__":
    print(p36solution1(1000000))