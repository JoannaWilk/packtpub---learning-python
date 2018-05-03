def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result


f5 = factorial(5)
f2 = factorial(2)
print(f5, f2)

print("-" * 12)

from functools import reduce
from operator import mul


def smarter_factorial(n):
    return reduce(mul, range(1, n+1), 1)
# last argument is not needed
# as a default it would take the first element from range (1, n+1)


f5 = smarter_factorial(5)
print(f5)
print("-" * 12)

print("returning multiple values")


def moddiv(a, b):
    return a // b, a % b


print(moddiv(20, 7))
