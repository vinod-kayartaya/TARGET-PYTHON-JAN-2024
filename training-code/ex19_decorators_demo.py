def uppercase(func):  # 'func' is the function on which this decorator is applied
    def fn(*args, **kwargs):  # *args is the arguments supplied to func
        args = tuple([a.upper() if type(a) is str else a for a in args])
        kwargs = {k: v.upper() if type(v) is str else v for k, v in kwargs.items()}
        func(*args, **kwargs)
    return fn


def line(char='-', count=50):  # arguments to the decorator e.g, @line('=', 30)
    def wrapper(func):  # 'func' is the function on which @line() is applied
        def modified_func(*args, **kwargs):  # args/kwargs - arguments to the function on which @line() is applied
            print(char*count)
            func(*args, **kwargs)
            print(char*count)
        return modified_func
    return wrapper


@line('_.')
@uppercase  # returns 'fn' which is defined in line2
def say_hello(name, city):
    print(f'hello {name}! When did you come from {city}?')


@line(char='~', count=25)
@uppercase
def print_emp_data(name, salary, dept):
    print(f'Name       = {name}')
    print(f'Salary     = Rs.{salary}')
    print(f'Department = {dept}')


if __name__ == '__main__':
    say_hello('Robert', 'Dallas')
    print_emp_data('Rajesh', 200000, 'production')
    print_emp_data(salary=50000, dept='accounting', name='ramesh')
