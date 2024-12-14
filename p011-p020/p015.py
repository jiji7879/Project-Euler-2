import bigNumberHelperFunctions

def p15solution1(grid_size: int) -> int:
    # The number of steps to get to the bottom-right corner of an n x n grid is 2n steps
    # Hilariously, the number of ways to get to the next part of the grid looks similar to Pascal's triangle,
    # which is most similar to polynomial exponentiation.
    # In fact, exponentiation to the power of 2n will get us the number of ways to get to (x, y) in 2n steps, with our goal being (n, n).
    # Amazingly, the (n, n) value turns out to be the maximum of that 2n step restriction.
    polynomial_power = [1,1]
    for _ in range(2*grid_size-1):
        polynomial_power = bigNumberHelperFunctions.polynomial_multiplication(polynomial_power, [1,1])
    return max(polynomial_power)

if __name__ == "__main__":
    print(p15solution1(20))