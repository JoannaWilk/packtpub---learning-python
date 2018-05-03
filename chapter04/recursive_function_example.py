def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n


f1 = factorial(1)
f5 = factorial(5)

print(f1, f5)
