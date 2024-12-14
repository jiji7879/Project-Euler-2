import bigNumberHelperFunctions

def p25solution() -> list:
    x1 = [1]
    x2 = [1]
    count = 2
    while len(x2) < 1000:
        x3 = bigNumberHelperFunctions.big_number_addition(x1, x2)
        x1 = x2
        x2 = x3
        count += 1
    return count

if __name__ == "__main__":
    print(p25solution())