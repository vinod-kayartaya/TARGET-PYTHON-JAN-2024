from pprint import pprint


class Person:
    def __init__(self, **kwargs):
        # call the setters
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

    @property
    def name(self) -> str:
        return self.__name.upper() if self.__name is not None else self.__name

    @name.setter
    def name(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('name must be a str')
        if value is not None and len(value) > 25:
            raise ValueError('name cannot exceed 25 letters')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value is not None and type(value) is not int:
            raise TypeError('age must be an int')
        if value is not None and (value <0 or value > 150):
            raise ValueError('age must be between 0 and 150')

        self.__age = value

    def print(self):
        print(f'Name = {self.__name}')
        print(f'Age  = {self.__age}')
        print()


if __name__ == '__main__':
    p1 = Person(name='John', age=550)
    p2 = Person(name='Jane')

    p1.name = 'John'  # setter for 'name' called here
    p2.age = 59  # setter for 'age' called here
    # Person.age(p2, 9999)

    print(f'{p1.name} is {p1.age} years old')

    Person.print(p1)  # p1 is passed as an argument explicitly
    p2.print()  # p2 is passed as an argument implicitly

