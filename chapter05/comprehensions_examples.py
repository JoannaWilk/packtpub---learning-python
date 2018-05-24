print('-' * 20)
print("LIST COMPREHENSIONS")
print('-' * 20)

# not a good example:
# squares = []
# for n in range(10):
#     squares.append(n ** 2)
# print(squares)

# a better example:
# squares = map(lambda n: n**2, range(10))
# print(list(squares))

# and the one with list comprehension:
print("[n ** 2 for n in range(10)]:\n",
      [n ** 2 for n in range(10)])
print('-' * 10)

# now only even squares

# 'so so' example
# even_squares = list(
#     filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10)))
# )

# list comprehension example:
even_squares = [n ** 2 for n in range(10) if not n % 2]
print("[n ** 2 for n in range(10) if not n % 2]:\n",
      [n ** 2 for n in range(10) if not n % 2])
print('\n')
print('-' * 10)
print("Nested comprehensions")
print('-' * 10)
items = 'ABCDE'

# bad example
# pairs = []
# for a in range(len(items)):
#     for b in range(a, len(items)):
#         pairs.append((items[a], items[b]))

pairs = [(items[a], items[b])
         for a in range(len(items)) for b in range(a, len(items))]
print("[(items[a], items[b])\n"
      "for a in range(len(items)) for b in range(a, len(items))]:\n",
      pairs)

print('\n')
print('-' * 10)
print("Filtering a comprehension")
print('-' * 10)
print("Find all Pythagorean triples with short side as numbers smaller than 10!")
from math import sqrt
# generate all possible pairs
mx = 10
pairs = [(a, b, sqrt(a**2 + b**2))
        for a in range(1, mx) for b in range(a, mx)]
print("all pairs:\n",
      pairs)
# filter out non Pythagorean triples
legs = list(
    filter(lambda triple: triple[2].is_integer(), pairs)
)
print(legs)
# make the third number an integer instead of float
legs = list(
    map(lambda triple: triple[:2] + (int(triple[2]), ), legs)
)
print(legs)
# lets do in one step :)
one_step_legs = [(a, b, int(c)) for a, b, c in pairs if c.is_integer()]
print(one_step_legs)

print("\n")
print('-' * 20)
print("DICT COMPREHENSIONS")
print('-' * 20)

from string import ascii_lowercase
print("dict((c, k) for k, c in enumerate(ascii_lowercase, 1))\n",
      dict((c, k) for k, c in enumerate(ascii_lowercase, 1)))
print('-' * 10)
print("{c: k for k, c in enumerate(ascii_lowercase, 1)}\n",
      {c: k for k, c in enumerate(ascii_lowercase, 1)})
print('-' * 10)
print("{c: c.swapcase() for c in 'Hello'}:\n",
      {c: c.swapcase() for c in 'Hello'})
print('-' * 10)
print("{c: k for k, c in enumerate('Hello')}:\n",
      {c: k for k, c in enumerate('Hello')})

print("\n")
print('-' * 20)
print("SET COMPREHENSIONS")
print('-' * 20)
print("set(c for c in 'Hello'):\n",
      set(c for c in 'Hello'))
print("{c for c in 'Hello'}:\n",
      {c for c in 'Hello'})
