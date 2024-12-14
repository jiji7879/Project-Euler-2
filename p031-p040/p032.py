import miscHelperFunctions

def pandigital_products() -> set:
    pandigital_product_set = set()
    for a in range(1, 9999):
        if not miscHelperFunctions.is_pandigital([a], True):
            continue
        for b in range(a, 9999):
            c = a * b
            if len(str(c)) + len(str(a)) + len(str(b)) > 9:
                break
            if miscHelperFunctions.is_pandigital([a, b, c], False):
                pandigital_product_set.add(c)
    return pandigital_product_set

def p32solution1() -> int:
    sum1 = 0
    products = pandigital_products()
    for number in products:
        sum1 += number
    return sum1

if __name__ == "__main__":
    print(p32solution1())