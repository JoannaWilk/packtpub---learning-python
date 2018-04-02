
print("empty list created by []: ", [])
print("empty list created by list(): ", list())
print("list: ", [1, 2, 3])

list_comprehension = """
list comprehension
[x + 5 for x in [2, 3, 4]]
gives: """
print(list_comprehension,
      [x + 5 for x in [2, 3, 4]])

list_from_tuple = """
list from a tuple (1, 2, 3)
list((1, 2, 3))
gives: """
print(list_from_tuple, list((1, 2, 3)))

list_from_string = """
list from a string 'hello'
list('hello')
gives: """
print(list_from_string, list('hello'))

print('\n------------------------------\n')

a = [1, 2, 1, 3]
print("list a =", a)
a.append(13)
print("a.append(13), a:", a)
print("count '1' in the list a by a.count(1):", a.count(1))
a.extend([5, 7])
print("\nextend list a by another list or sequence"
      "\nby a.extend([5, 7]). a:", a, "\n")

print("position of '13' in the list by a.index(13):", a.index(13))
a.insert(0, 17)
print("\ninsert '17' at position 0"
      "\nby a.insert(0, 17). a:", a, "\n")
print("pop - remove and return"
      "\nlast element by a.pop():", a.pop(),
      "\nelement at position 3 by a.pop(3):", a.pop(3))
print("\nnow list a looks like this:", a)
a.remove(17)
print("\nremove '17' from list by a.remove(17). a:", a)
a.reverse()
print("\nreverse list by a.reverse(). a:", a)
a.sort()
print("sort list by a.sort(). a:", a)
a.clear()
print("\nremove all elements from the list"
      "\nby a.clear(). a:", a)

print('\n------------------------------\n')

a = list('hello')
print("a = list('hello'):", a)
a.append(100)
print("a.append(100). a:", a)
a.extend((1, 2, 3))
print("a.extend((1, 2, 3)). a:", a)
a.extend('...')
print("a.extend('...'). a:", a)

print('\n------------------------------\n')

a = [1, 3, 5, 7]

print("list a:", a)
print("min(a):", min(a))
print("max(a):", max(a))
print("sum(a):", sum(a))
print("number of elements by len(a):", len(a))

b = [6, 7, 8]
print("\nlist a:", a,
      "\nlist b:", b)
print("a + b:", a + b)
print("a * 2:", a * 2)

print('\n------------------------------\n')

from operator import itemgetter

a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print("list a:", a)
print("sorted(a):", sorted(a))
print("sorted(a, key=itemgetter(0)):\n", sorted(a, key=itemgetter(0)))
print("sorted(a, key=itemgetter(0, 1)):\n", sorted(a, key=itemgetter(0, 1)))
print("sorted(a, key=itemgetter(1):\n", sorted(a, key=itemgetter(1)))
print("sorted(a, key=itemgetter(1), reverse=True):\n", sorted(a, key=itemgetter(1), reverse=True))
