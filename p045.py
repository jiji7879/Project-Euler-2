def triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def pentagonal_number(n: int) -> int:
    return n * (3 * n - 1) // 2


def hexagonal_number(n: int) -> int:
    return n * (2 * n - 1)


def p45solution1() -> int:
    i = 286
    j = 1
    k = 1
    triangle = triangle_number(i)
    pentagon = pentagonal_number(j)
    hexagon = hexagonal_number(k)
    # we are assured that this stops
    while pentagon != hexagon or triangle != pentagon:
        while triangle != pentagon:
            if triangle < pentagon:
                i += 1
                triangle = triangle_number(i)
            elif triangle > pentagon:
                j += 1
                pentagon = pentagonal_number(j)
        while pentagon != hexagon:
            if pentagon < hexagon:
                j += 1
                pentagon = pentagonal_number(j)
            elif pentagon > hexagon:
                k += 1
                hexagon = hexagonal_number(k)
    return triangle


if __name__ == "__main__":
    print(p45solution1())
