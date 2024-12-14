def special_pythagorean_triplet(num: int) -> (int, int, int):
    for a in range(1, num // 3 + 1):
        for b in range(a + 1, num // 2 + 1):
            c = num - a - b
            if a * a + b * b == c * c:
                return a, b, c
    return -1, -1, -1


def p9solution1() -> int:
    a, b, c = special_pythagorean_triplet(1000)
    if a == -1:
        return False
    else:
        return a * b * c

if __name__ == "__main__":
    print(p9solution1())