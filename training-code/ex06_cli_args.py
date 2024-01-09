import sys
import my_utils


if __name__ == '__main__':
    print('command line args demo')
    sys.argv.pop(0)
    nums = [float(n) for n in sys.argv if my_utils.is_float(n)]
    print(nums)
    print(sum(nums))

