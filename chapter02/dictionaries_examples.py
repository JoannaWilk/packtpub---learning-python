a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})

print("a = dict(A=1, Z=-1)\n", a)
print("---------------------------")

print("b = {'A': 1, 'Z': -1}\n", b)
print("---------------------------")

print("c = dict(zip(['A', 'Z'], [1, -1]))\n", c)
print("---------------------------")

print("d = dict([('A', 1), ('Z', -1)])\n", d)
print("---------------------------")

print("e = dict({'Z': -1, 'A': 1})\n", e)
print("---------------------------")

print("a == b == c == d == e: ", a == b == c == d == e)

print("\n---------------------------\n")

d = {}
print("dictionary d:", d)
d['a'] = 1
d['b'] = 2
print("d['a'] = 1\nd['b'] = 2")
print("len(d):", len(d))
print("d['a']:", d['a'])
print("dictionary d:", d)
del d['a']
print("del d['a']. d:", d)
d['c'] = 3
print("d['c'] = 3")
print("'c' in d:", 'c' in d)
print("3 in d:", 3 in d)
print("'e' in d:", 'e' in d)
d.clear()
print("d.clear(). d:", d)

print("\n---------------------------\n")

d = dict(zip('hello', range(5)))
print("d = dict(zip('hello', range(5)))")
print('d:', d)
print('d.keys():', d.keys())
print('d.values():', d.values())
print('d.items():', d.items())
print('3 in d.values():', 3 in d.values())
print("('o', 4) in d.items():", ('o', 4) in d.items())

print("\n---------------------------\n")

print("d = dict(zip('hello', range(5)))")
print('d:', d)
print("d.popitem():", d.popitem())
print('d:', d)
print("d.pop('l'):", d.pop('l'))
# this will cause an error
# print("d.pop('not-a-key'):", d.pop('not-a-key'))
d.update({'another': 'value'})
d.update(a=13)
print("d.update({'another': 'value'})")
print("d.update(a=13)")
print('d:', d)
print("d.get('a'):", d.get('a'))
print("if key 'a' is missing, return default value 177\n"
      "d.get('a', 177):", d.get('a', 177))
print("if key 'b' is missing, return default value 177\n"
      "d.get('b', 177):", d.get('b', 177))
print("d.get('b'):", d.get('b'))

print("\n---------------------------\n")

d = {}
print("d = {}. d:", d)
d.setdefault('a', 1)
print("if key 'a' is missing, create it and set value 1\n"
      "d.setdefault('a', 1). d:", d)
print("if key 'a' is missing, create it and set value 5\n"
      "d.setdefault('a', 5). d:", d)
print("if a key exists it can not be overwritten with this method")

print("\n---------------------------\n")

print("test:")
d = {}
print("d = {}")
d.setdefault('a', {}).setdefault('b', []).append(1)
print("d.setdefault('a', {}).setdefault('b', []).append(1)")
print("d:", d)
