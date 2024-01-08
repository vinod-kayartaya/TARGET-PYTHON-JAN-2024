"""
this module contains examples for user defined functions
"""


def greet(name: str = 'friend', city: str = 'your city') -> None:
    print(f'Hello {name}! How is weather in {city}?')


def say_hello() -> None:
    """
    just prints a greeting message
    :return: None
    """
    print('Hello, world!')


if __name__ == '__main__':
    say_hello()
    greet('Vinod', 'Bangalore')
    greet(city='Nagpur', name='Nived')
    greet('Uday')
    greet()

