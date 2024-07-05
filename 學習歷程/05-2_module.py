def foo():
    print('hello,module')


def add(*args):
    value = 0
    for i in args:
        value += i
        print('module')
    return value
