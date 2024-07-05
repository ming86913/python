def Hello():
    print('hello,function module')


def add(*args):
    value = 0
    for i in args:
        value += i
        print('module')
    return value
