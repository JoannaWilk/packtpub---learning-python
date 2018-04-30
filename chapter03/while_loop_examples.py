# binary example


n = 39
print('binary representation of n = ', n)
print("remainders = []\n"
      "while n > 0:\n"
      "    remainder = n % 2\n"
      "    remainders.append(remainder)\n"
      "    n //= 2\n"
      "remainders_reversed = remainders[::-1]")
remainders = []
while n > 0:
    remainder = n % 2
    remainders.append(remainder)
    n //= 2
remainders_reversed = remainders[::-1]
print('reversed remainders:', remainders_reversed)

print("\n-----------------------\n")

n = 39
print('binary representation of n = ', n)
print("remainders = []\n"
      "while n > 0:\n"
      "    n, remainder = divmod(n, 2)\n"
      "    remainders.append(remainder)\n"
      "remainders_reversed = remainders[::-1]")
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
remainders_reversed = remainders[::-1]
print('reversed remainders:', remainders_reversed)
