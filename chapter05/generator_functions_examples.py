# classic function approach
def get_squares(n):
    return [x ** 2 for x in range(n)]


print("def get_squares(n):\n"
      "    return [x ** 2 for x in range(n)]\n")
print("get_squares(10):\n",
      get_squares(10))
print("-" * 10)


# generator approach
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


print("def get_squares_gen(n):\n"
      "    for x in range(n):\n"
      "        yield x ** 2\n")
print("list(get_squares_gen(10)):\n",
      list(get_squares_gen(10)))
squares = get_squares_gen(4)
print("squares = get_squares_gen(4)")
print("squares:", squares)
print("next(squares):", next(squares))
print("next(squares):", next(squares))
print("next(squares):", next(squares))
print("next(squares):", next(squares))
# line below raises a StopIteration Error
# print("next(squares):", next(squares))
squares = get_squares_gen(3)
print("\nsquares = get_squares_gen(3)")
print("squares:", squares)
print("squares.__next__():", squares.__next__())
print("squares.__next__():", squares.__next__())
print("squares.__next__():", squares.__next__())
# line below raises a StopIteration Error
# print("squares.__next__():", squares.__next__())
print("-" * 10)


def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1


print("def geometric_progression(a, q):\n"
      "    k = 0\n"
      "    while True:\n"
      "        result = a * q**k\n"
      "        if result <= 100000:\n"
      "            yield result\n"
      "        else:\n"
      "            return\n"
      "        k += 1")

print("\nfor n in geometric_progression(2, 5):\n"
      "    print(n)")

for n in geometric_progression(2, 5):
    print(n)

print("-" * 10)


def counter(start=0):
    x = start
    while True:
        yield x
        x += 1


c = counter()

print("def counter(start=0):\n"
      "    x = start\n"
      "    while True:\n"
      "        yield x\n"
      "        x += 1")
print("\nc = counter()")
print("next(c):", next(c))
print("next(c):", next(c))
print("next(c):", next(c))


print("-" * 10)


stop = False
def counter(start=0):
    x = start
    while not stop:
        yield x
        x += 1


c = counter()

print("stop = False\n"
      "def counter(start=0):\n"
      "    x = start\n"
      "    while not stop:\n"
      "        yield x\n"
      "        x += 1")
print("\nc = counter()")
print("next(c):", next(c))
print("next(c):", next(c))
stop = True
print("stop = True")
# the line below will raise an error
# print("next(c):", next(c))

print("-" * 10)


def counter(start=0):
    x = start
    while True:
        result = yield x
        print(type(result), result)
        if result == 'Q':
            break
        x += 1


print("def counter(start=0):\n"
      "    x = start\n"
      "    while True:\n"
      "        result = yield x\n"
      "        print(type(result), result)\n"
      "        if result == 'Q':\n"
      "            break\n"
      "        x += 1")

c = counter()
print("c = counter()")
print("next(c):", next(c))
print("c.send('Wow!'):", c.send('Wow!'))
print("c.send('Oopsie!'):", c.send('Ooopsie!'))
print("next(c):", next(c))
print("next(c):", next(c))
print("next(c):", next(c))
# line below raises StopIterationError
# print("c.send('Q'):", c.send('Q'))

print("-" * 10)


def print_squares(start, end):
    # for x in range(start, end):
    #     yield x ** 2
    yield from (x ** 2 for x in range(start, end))


for n in print_squares(2, 5):
    print(n)

