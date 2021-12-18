def float_or_int(num):
    try:
        if num.is_integer():
            return int(num)
        else:
            return num
    except AttributeError:
        return num


def try_int(num_str):
    try:
        num_str = int(num_str)
        return num_str
    except ValueError:
        return float(num_str)


def get_numbers():
    with open('numbers.csv') as file:
        numbers_list = []
        for line in file:
            numbers_line_list = line.strip("\n").split(" ")
            for number in numbers_line_list:
                if number != '':
                    numbers_list.append(try_int(number))
    return numbers_list


def minimum_of_nums(numbers_list):
    try:
        min_num = numbers_list[0]
        for num in numbers_list:
            if num < min_num:
                min_num = num
        return float_or_int(min_num)
    except OverflowError:
        return 'inf'


def maximum_of_nums(numbers_list):
    try:
        max_num = numbers_list[0]
        for num in numbers_list:
            if num > max_num:
                max_num = num
        return float_or_int(max_num)
    except OverflowError:
        return 'inf'


def sum_of_nums(numbers_list):
    try:
        sum_nums = 0.0
        for num in numbers_list:
            sum_nums += num
        return float_or_int(sum_nums)
    except OverflowError:
        return 'inf'


def multiplication_of_nums(numbers_list):
    try:
        multiplication_nums = 1.0
        for num in numbers_list:
            multiplication_nums *= num
        return float_or_int(multiplication_nums)
    except OverflowError:
        return 'inf'


numbers = get_numbers()
minimum = minimum_of_nums(numbers)
maximum = maximum_of_nums(numbers)
summa = sum_of_nums(numbers)
multiplication = multiplication_of_nums(numbers)

# print('Минимальное:', minimum,
#       '\nМаксимальное:', maximum,
#       '\nСумма:', summa,
#       '\nПроизведение:', multiplication,)
