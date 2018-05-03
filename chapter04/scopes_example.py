def outer():
    # the line below produces an error
    # because the nearest enclosing scope is global
    # which is excluded for nonlocal statement
    # nonlocal test
    test = 1

    def inner():
        # nonlocal test
        global test
        test = 2
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0
outer()
print('global:', test)
