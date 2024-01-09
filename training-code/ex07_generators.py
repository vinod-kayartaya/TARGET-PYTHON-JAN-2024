"""
a generator is a function that can return (yield) a value to the caller, and when you call
the generator function again, it will resume from the last return (yielded) statement.
"""


def fibo(limit=10):
    """
    fibonacci elements are 0, 1, 1, 2, 3, 5, 8, 13, ...
    :param limit: how many elements you want?
    """
    print('start of fibo() function')
    a, b = -1, 1
    for _ in range(limit):
        c = a + b
        yield c  # give this value to the caller
        a, b = b, c


def main():
    f = fibo(15)
    print(f'type of f is {type(f)}')
    print(f'f is {f}')
    for c in f:  # c = next(f)
        print(c, end=", ")

    print()


if __name__ == '__main__':
    main()