print('create list of all the numbers up to N\n'
      'which are multiplies of 5')
print('-' * 10)


def is_multiple_of_five(n):
    return not n % 5


def get_multiples_of_five_without_lambda(n):
    return list(filter(is_multiple_of_five, range(n)))


print("get_multiples_of_five_without_lambda(50):\n",
      get_multiples_of_five_without_lambda(50))
print('-' * 10)


def get_multiples_of_five_with_lambda(n):
    return list(filter(lambda k: not k % 5, range(n)))


print("get_multiples_of_five_with_lambda(50):\n",
      get_multiples_of_five_with_lambda(50))
print('-' * 10)


# function below
def adder(a, b):
    return a + b
# is equivalent to:
# lambda a, b: a + b


def to_upper(s):
    return s.upper()
# lambda s: s.upper()
