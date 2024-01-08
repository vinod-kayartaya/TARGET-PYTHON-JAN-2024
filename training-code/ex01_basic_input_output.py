"""
the value of __name__ is '__main__' if the current module is run directly.
if the module is imported in another file, then the value of __name__ is
the base name of the file
"""

print(f'inside ex01_basic_input_output.py, value of __name__ is {__name__}')

if __name__ == '__main__':

    user_name = input('What is your name? ')
    user_city = input('Where do you live? ')
    user_age = int(input('How old are you? '))

    print(f'Hello {user_name}! How is weather in {user_city}?')
    print(f'Next year you will be {1+user_age} years old.')

