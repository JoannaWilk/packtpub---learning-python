grades = [18, 23, 30, 27, 15, 9, 22]
avgs = [22, 21, 29, 24, 18, 18, 24]
print("list(zip(avgs, grades)):\n",
      list(zip(avgs, grades)))
print('-' * 10)
print(
    "list(map(lambda *a: a, avgs, grades)):\n",
    list(map(lambda *a: a, avgs, grades))
)

print('\n', '-' * 10, '\n')

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]
maxs = map(lambda n: max(*n), zip(a, b, c))
print("list(map(lambda n: max(*n), zip(a, b, c))):\n",
      list(maxs))
