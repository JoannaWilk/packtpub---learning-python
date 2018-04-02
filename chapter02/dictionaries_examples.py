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
