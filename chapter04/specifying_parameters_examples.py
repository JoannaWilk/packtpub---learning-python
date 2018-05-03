def positional(a, b, c):
    print(a, b, c)


print('\npositional(1, 2, 3)')
positional(1, 2, 3)


def keyword(a, b=4, c=88):
    print(a, b, c)


print('\nkeyword(a=1, c=2, b=3)')
keyword(a=1, c=2, b=3)

print('\nkeyword(1)')
keyword(1)

print('\nkeyword(42, c=9)')
keyword(42, c=9)

print('\nvariable positional arguments')
print("-----------------------")
print('find minimum example:')


def minimum(*args):
    print('args:', args)
    if args:
        mn = args[0]
        for value in args[1:]:
            if value < mn:
                mn = value
        print('minimum:', mn)


minimum(1, 3, -7, 9)
minimum()


def func(*args):
    print(args)


print("-----------------------")
print("def func(*args):\n"
      "    print(args)")
values = (1, 3, -7, 9)
print("func(values):")
func(values)
print("unpacking -> func(*values):")
func(*values)


print('\nvariable keyword arguments')
print("-----------------------")
print('def kfunc(**kwargs):\n'
      '    print(kwargs)')


def kfunc(**kwargs):
    print(kwargs)


print("kfunc(a=1, b=42):")
kfunc(a=1, b=42)
print("unpacking dict -> kfunc(**{'a': 1, 'b': 42}):")
kfunc(**{'a': 1, 'b': 42})
print("unpacking dict -> kfunc(**dict(a=1, b=42)):")
kfunc(**dict(a=1, b=42))
print("-----------------------")
print("connect to db example:")


def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)


connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='asia', pwd='gandalf')

print('\nkeyword-only arguments')
print("-----------------------")
print('def kwofunc(*a, c):\n'
      '    print(a, c)')


def kwofunc(*a, c):
    print(a, c)


print("kwofunc(1, 2, 3, c=7):")
kwofunc(1, 2, 3, c=7)
print("kwofunc(c=4)")
kwofunc(c=4)
print("kwofunc(1, 2) produces error, because the 'c' is not specified")
print("-----------------------")
print('def other_kwofunc(a, b=42, *, c):\n'
      '    print(a, b, c)')


def other_kwofunc(a, b=42, *, c):
    print(a, b, c)


print("other_kwofunc(3, b=7, c=99)")
other_kwofunc(3, b=7, c=99)
print("other_kwofunc(3, c=13)")
other_kwofunc(3, c=13)
print("other_kwofunc(3, 23) produces error, because the 'c' is not specified")

print('\ncombining arguments types')
print("-----------------------")


def comb_func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


print("comb_func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'}):")
comb_func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
print("-----------------------")
print("comb_func(1, 2, 3, 5, 7, 9, A='a', B='b'):")
comb_func(1, 2, 3, 5, 7, 9, A='a', B='b')
print("-----------------------")


def comb_kwonly_func(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)


print("comb_kwonly_func(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F'):")
comb_kwonly_func(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
print("-----------------------")
print("comb_kwonly_func(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F'):")
comb_kwonly_func(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')

print('\nTRAP! mutable default arguments types')
print("-----------------------")


def trap_func(a=[], b={}):
    print(a)
    print(b)
    print("#" * 12)
    a.append(len(a))
    b[len(a)] = len(a)


trap_func()
trap_func(a=[1, 2, 3], b={'B': 1})
trap_func()
trap_func()


# so to avoid trap, we can use this:
def convention_func(a=None):
    if a is None:
        a = []
