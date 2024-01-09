def fn():
    print('start of fn()')
    yield 100
    print('sending 200')
    yield 200
    print('sending 300')
    yield 300
    print('sending 400')
    yield 500

if __name__ == '__main__':
    f = fn()
    print(f'type of f is {type(f)}')
    n = next(f)
    print(f'n is {n}')
    while True:
        try:
            n = next(f)
            print(f'n is {n}')
        except StopIteration:
            break
    print('that\'s all folks!')
