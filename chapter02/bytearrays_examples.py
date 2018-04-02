print("empty bytearray object by bytearray():", bytearray())

print("\nzero-filled instance with given length by bytearray(10):\n",
      bytearray(10))
print("\nbytearray from iterable of integers by bytearray(range(5)):\n",
      bytearray(range(5)))
name = bytearray(b'Lina')
print("\nname = bytearray(b'Lina'):", name)
print("name.replace(b'L', b'l'):", name.replace(b'L', b'l'))
print("name.endswith(b'na'):", name.endswith(b'na'))
print("name.upper():", name.upper())
print("name.count(b'L'):", name.count(b'L'))
