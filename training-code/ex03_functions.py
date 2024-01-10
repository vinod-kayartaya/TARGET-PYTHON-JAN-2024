"""
this module contains examples for user defined functions
"""


def greet(name: str = 'friend', city: str = 'your city') -> None:
    if type(name) is not str or type(city) is not str:
        raise TypeError('name and city must be str')

    print(f'Hello {name}! How is weather in {city}?')


def say_hello() -> None:
    """
    just prints a greeting message
    :return: None
    """
    print('Hello, world!')


def add(*numbers) -> float:
    print(f'len(numbers) = {len(numbers)}')
    total = 0
    for each_num in numbers:
        if type(each_num) in (int, float):
            total += each_num
    return total


if __name__ == '__main__':
    # say_hello()
    # greet('Vinod', 'Bangalore')
    # greet(city='Nagpur', name='Nived')
    # greet('Uday')
    # greet(10)
    # n = add(10, 20.9, 'vinod', False, 30)  # you may pass any number of arguments
    # print(f'n is {n}')
    t = (10, 20, 30, 40)
    x = add(*t)
    print(f'x is {x}')
