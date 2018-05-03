x = 3


def func1(y):
    print(y)


def func2(x):
    x = 7


def func3(x):
    x[1] = 42
    x = 'another x'


func1(x)
func2(x)
print(x)

x = [1, 2, 3]
func3(x)
print(x)
