import helperFunctions

def p24solution1():
    permutation = helperFunctions.find_nth_lexicographic_permutation(list(range(10)), 1000000-1)
    string = ""
    for int in permutation:
        string += str(int)
    return string

if __name__ == "__main__":
    print(p24solution1())