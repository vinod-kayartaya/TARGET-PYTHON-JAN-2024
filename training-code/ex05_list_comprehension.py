from my_utils import max_days
from pprint import pprint


def main():
    nums = [10, 12, 29, 10, 49, 59, 29, 27, 58, 33]
    # nums2 = []
    # for each_num in nums:
    #     nums2.append(each_num * 2)

    nums2 = [
        each_num * 2            # what to append
        for each_num in nums    # source
    ]

    # even_nums = []
    # for each_num in nums:
    #     if each_num % 2 == 0:
    #         even_nums.append(each_num)
    even_nums = [
        each_num
        for each_num in nums
        if each_num % 2 == 0
    ]
    odd_nums = [n for n in nums if n % 2]

    print(nums)
    print(nums2)
    print(even_nums)
    print(odd_nums)

    year = 2023
    days_in_year = [(i, max_days(i, year)) for i in range(1, 13)]
    pprint(days_in_year)

    names = ['vinod kumar', 'SHYAM', 'ramesh iyer', 'rohit shetty', 'sunil kumar']

    first_names = [
        name[:name.index(' ')].title() if name.find(' ') != -1 else name.title()
        for name in names
    ]
    print(first_names)


if __name__ == '__main__':
    main()
