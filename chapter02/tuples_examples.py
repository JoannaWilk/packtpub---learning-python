# empty tuple
t = ()
print("empty tuple: ", t)
print("type of empty tuple: ", type(t))

# one element tuple
# there is comma needed to create it
one_element_tuple = (42, )
print("one element tuple (42, ): ", one_element_tuple)

three_elements_tuple = (1, 3, 5)
print("three elements tuple (1, 3, 5): ", three_elements_tuple)

# multiple assignment
a, b, c = 1, 2, 3

# implicit tuple to print with one instruction
# check in console
# a, b, c

print("test if 3 is in three elements tuple")
print("3 in three_elements_tuple: ", 3 in three_elements_tuple)

# swapping variables
a, b = 1, 2
c = a
a = b
b = c
traditional_swap = """traditional swapping:
a, b = 1, 2
c = a
a = b
b = c
print(a, b): """
print(traditional_swap, a, b)

print('------------------')

a, b = 1, 2
a, b = b, a
pythonic_swap = """pythonic swapping:
a, b = 1, 2
a, b = b, a
print(a, b): """
print(pythonic_swap, a, b)
