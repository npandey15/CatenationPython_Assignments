def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

# The output of the above program will display error "NameError: global name 'f' is not defined"
