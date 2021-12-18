def try_int(num):
    if num.is_integer():
        return int(num)
    else:
        return num


def get_numbers():
    with open('numbers.csv') as file:
        numbers_list = []
        for line in file:
            numbers_line_list = line.strip("\n").split(" ")
            for number in numbers_line_list:
                if number != '':
                    numbers_list.append(float(number))
    return numbers_list


def minimum_of_nums(numbers_list):
    min_num = numbers_list[0]
    for num in numbers_list:
        if num < min_num:
            min_num = num
    return try_int(min_num)


def maximum_of_nums(numbers_list):
    max_num = numbers_list[0]
    for num in numbers_list:
        if num > max_num:
            max_num = num
    return try_int(max_num)


def sum_of_nums(numbers_list):
    sum_nums = 0.0
    for num in numbers_list:
        sum_nums += num
    return try_int(sum_nums)


def multiplication_of_nums(numbers_list):
    multiplication_nums = 1.0
    for num in numbers_list:
        multiplication_nums *= num
    return try_int(multiplication_nums)


numbers = get_numbers()
minimum = minimum_of_nums(numbers)
maximum = maximum_of_nums(numbers)
summa = sum_of_nums(numbers)
multiplication = multiplication_of_nums(numbers)

# print('Минимальное:', minimum,
#       '\nМаксимальное:', maximum,
#       '\nСумма:', summa,
#       '\nПроизведение:', multiplication,)
