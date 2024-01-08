def main():
    # nums = list((10, 12, 29, 10, 49, 59, 29, 27, 58, 33))
    nums = [10, 12, 29, 10, 49, 59, 29, 27, 58, 33]
    print(f'there are {len(nums)} elements in the list nums')
    my_name = 'vinod kumar k'
    print(f'my_name has {len(my_name)} letters')

    index = 4
    print(f'element at index {index} of nums is {nums[index]}')
    ele_count = 3
    print(f'{ele_count} elements from index {index} of nums is {nums[index: index+ele_count]}')
    print(f'all elements starting from index {index} of nums is {nums[4:len(nums)]}')
    print(f'all elements starting from index {index} of nums is {nums[4:]}')
    print(f'all elements starting from index 0 till index {index} of nums is {nums[0:index]}')
    print(f'all elements starting from index 0 till index {index} of nums is {nums[:index]}')
    print(f'all elements in nums is {nums}')
    print(f'all elements in nums is {nums[0:len(nums)]}')
    print(f'all elements in nums is {nums[:]}')

    first_name = my_name[:my_name.index(' ')]
    print(f'first_name is {first_name}')

    filename = '/Users/vinod/Desktop/customers.csv'
    xml_filename = filename[:-3] + 'xml'
    print(f'xml_filename is {xml_filename}')

    print(nums[::])  # [from_index: to_index: step=1]
    print(nums[::2])  # elements at even indices
    print(nums[1::2])  # elements at odd indices
    print(nums[::-1])  # reverse order
    print(nums[len(nums)::-1])
    print(nums[5:2:-1])
    print(nums[-5:2:-1])
    print(nums[5:-8:-1])
    print(nums[-5:-8:-1])
    print(my_name[::-1])

    print('-'*50)
    print(nums)
    nums[3:5] = [100, 200, 300, 400]
    print(nums)


if __name__ == '__main__':
    main()
