# Doing this by pen and paper...
# Case 1: suppose that the ones are the same.
# Then we need to find a, b, c such that (a*10 + c)/(b*10 + c) = a/b
# b(a*10 + c) = a(b*10 + c) means bc=ac, so a=b except if c=0. If c=0, the case is trivial. If a=b, the case is also trivial.
# Case 2: suppose that the tens are the same.
# We need to find a,b,c such that (a*10 + b)/(a*10 + c) = b/c
# Again, c(a*10 + b) = b(a*10 + c) so ca*10 = ba*10 which means ca = ba. a=0 is trivial, and so is b=c.
# Case 3: Suppose there exists a, b, cand c such that (a*10 + c)/(c*10 + b) = a/b.
# Then b(a*10 + c) = a(c*10 + b) so b*a*10 + b*c = a*c*10 + a*b.

import primeHelperFunctions


def p33solution1() -> int:
    numerator = 1
    denominator = 1
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(10):
                if b * a * 10 + b * c == a * c * 10 + a * b:
                    # (a*10+c)/(c*10+b) = a/b
                    numerator *= a
                    denominator *= b
    gcd1 = primeHelperFunctions.gcd(numerator, denominator)
    return denominator // gcd1


if __name__ == "__main__":
    print(p33solution1())
