import threading
from threading import Thread


def foo():
    print('inside foo...')
    print(f'name of the current thread is {threading.current_thread().name}')
    bar()


def bar():
    print('inside bar')
    print(f'name of the current thread is {threading.current_thread().name}')


def start():
    print(f'name of the current thread is {threading.current_thread().name}')
    foo()
    bar()
    t1 = Thread(target=foo, name='t1')
    t2 = Thread(target=bar, name='t2')
    t1.start()
    t2.start()


if __name__ == '__main__':
    start()
