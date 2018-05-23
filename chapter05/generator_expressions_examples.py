cubes = [k ** 3 for k in range(10)]
print("cubes = [k ** 3 for k in range(10)]:\n"
      "cubes:", cubes)
print("type(cubes):", type(cubes))

cubes_gen = (k ** 3 for k in range(10))
print("\ncubes_gen = (k ** 3 for k in range(10)):\n"
      "cubes_gen:", cubes_gen)
print("type(cubes_gen):", type(cubes_gen))
print("list(cubes_gen):", list(cubes_gen))
print("list(cubes_gen):", list(cubes_gen))

odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)
print('odd cubes:', list(odd_cubes1))
print('odd cubes:', list(odd_cubes2))
print('-' * 10)


def adder(*n):
    return sum(n)


s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s1)
print(s2)
print('-' * 10)


N = 20
cubes1 = map(
    lambda n: (n, n**3),
    filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N))
)
cubes2 = (
    (n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0
)
print(list(cubes1))
print(list(cubes2))
