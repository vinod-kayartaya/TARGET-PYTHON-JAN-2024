import time
from threading import Thread


def do_stuff(name, city, count=10, delay=100):
    for i in range(count):
        print(f'hello {name}, how is weather in {city}')
        time.sleep(delay/1000)


def main():
    t1 = Thread(target=do_stuff, args=('ramesh', 'chennai'))  # target(*args)
    t2 = Thread(target=do_stuff, args=('sujeeth', 'mangalore', 150000, 75), daemon=False)

    t1.start()
    t2.start()
    print('end of main()')


if __name__ == '__main__':
    main()
