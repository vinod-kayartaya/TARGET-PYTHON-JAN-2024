FILENAME = '/Users/vinod/Desktop/TARGET-PYTHON-JAN-2024/training-code/my_utils.py'


def read_file_method1():
    f = None
    try:
        f = open(FILENAME)
        content = f.read()
        print(content)
    except OSError as e:
        print(f'there was an error - {e}')
    finally:
        if f is not None:
            f.close()


def read_file_method2():
    try:
        with open(FILENAME) as f:
            content = f.read()
            print(content)
            # just here f.close() is automatically called
    except OSError as e:
        print(f'there was an error - {e}')


def read_file_method3():
    try:
        with open(FILENAME) as f:
            while True:
                a_line = f.readline()
                if a_line == '':
                    break
                print(a_line, end='')
            print()
    except OSError as e:
        print(f'there was an error - {e}')


def read_file_method4():
    try:
        with open(FILENAME) as f:
            for a_line in f:  # f is a stream of lines
                print(a_line, end='')
            print()
    except OSError as e:
        print(f'there was an error - {e}')


if __name__ == '__main__':
    read_file_method4()
