class Person:
    def __init__(self, name: str = '', age: int = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name="{self.name}", age={self.age})'

    def __iadd__(self, value):
        if type(value) in (int, float):
            self.age += value
        elif type(value) is str:
            self.name += value
        else:
            raise TypeError('Invalid type for += (int/float/str is expected)')
        return self

    def __isub__(self, value):
        if type(value) in (int, float):
            self.age -= value
        else:
            raise TypeError('Invalid type for -= (int/float is expected)')
        return self

    def __eq__(self, other):  # __ne__ is implicit here
        if not isinstance(other, Person):
            return False
        if id(self) == id(other):
            return True

        return self.name == other.name \
            and self.age == other.age


if __name__ == '__main__':
    p1 = Person('Vinod', 50)
    p2 = Person('Shyam', 45)
    p3 = Person('Shyam', 45)
    p4 = p2

    print(p2 == p1)
    print(p2 == p3)
    print(p2 == p4)
    print(p2 == 'Shyam')

    p1 -= 5.1  # p1.__isub__(5.1)
    p1 += 1.3  # p1.__iadd__(1.3)
    p1 += ' Kumar'  # p1.__iadd__(' Kumar')
    # p1 += False
    print(p1)


