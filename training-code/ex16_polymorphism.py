from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def talk(self) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    def run(self):
        # self.name() is taken from the subclass
        print(f'{self.name()} is running...')


class Cat(Animal):
    def talk(self) -> None:
        print('meow...')
    
    def name(self) -> str:
        return 'cat'


class Dog(Animal):
    def talk(self) -> None:
        print('bow bow...')

    def name(self) -> str:
        return 'dog'


class Lion(Animal):
    def talk(self) -> None:
        print('Grrrr...')

    def name(self) -> str:
        return 'lion'


# polymorphic method
def process_animal(animal) -> None:
    if not isinstance(animal, Animal):
        raise TypeError('Must pass an Animal object')
    animal.talk()
    animal.run()


if __name__ == '__main__':
    c1 = Cat()  # instance of Cat, Animal, object
    l1 = Lion()  # instance of Lion, Animal, object
    d1 = Dog()  # instance of Dog, Animal, object
    s1 = 'Vinod'  # instance of str, object
    process_animal(c1)
    process_animal(l1)
    process_animal(d1)
    process_animal(s1)  # error  
