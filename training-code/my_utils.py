def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


def max_days(month: int, year: int) -> int:
    if 1 <= month <= 12:
        if year > 0:
            if month == 2:
                return 29 if is_leap(year) else 28
            elif month in (4, 6, 9, 11):
                return 30
            return 31
        else:
            raise ValueError('year must be > 0')
    else:
        raise ValueError('month must be between 1 and 12')


def factorial(num: int) -> int:
    if type(num) is not int:
        raise TypeError(f'num must be int, but got {type(num)}')
    if num < 0:
        raise ValueError('num must be > 0')
    f = 1
    while num:
        f *= num
        num -= 1
    return f


def is_float(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def dir2(obj) -> list:
    return [
        each_attr
        for each_attr in dir(obj)
        if not each_attr.startswith('_')
    ]


if __name__ == '__main__':
    print(max_days(1, 2024))
    print(factorial(10))
