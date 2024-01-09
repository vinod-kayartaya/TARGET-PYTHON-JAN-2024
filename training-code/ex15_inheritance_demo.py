from my_utils import dir2


class Resource:
    def __init__(self, **kwargs):
        self.resource_type = kwargs.get('resource_type')

    def print(self):
        print(f'Type    : {self.resource_type}')


class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Name    : {self.name}')
        print(f'Email   : {self.email}')


class Employee(Resource, Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Person.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    def print(self):
        print(f'Id      : {self.id}')
        Person.print(self)
        print(f'Salary  : {self.salary}')
        super().print()

    def dict(self):
        return self.__dict__


if __name__ == '__main__':
    e1 = Employee(id=1122, name='john', email='john@xmpl.com', salary=50000, resource_type='human')
    print(dir2(e1))
    e1.print()
    print(e1.dict())
    print(Employee.mro())
