# Name: Michelle Alexandra Loya
# OSU Email: loyami@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 4/24/23
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    This function receives a one-dimensional array of integers and returns a Python
    tuple with two values - the minimum and maximum values of the input array.
    """

    min = arr[0]
    max = min

    for index in range(arr.length()):
        if arr[index] < min:
            min = arr[index]
        elif arr[index] > max:
            max = arr[index]

    result = (min, max)

    return result


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray of integers and returns a new StaticArray object
    with the content of the original array, modified as follows:
        1) If the number in the original array is divisible by 3, the corresponding element in the
           new array will be the string ‘fizz’.
        2) If the number in the original array is divisible by 5, the corresponding element in the
           new array will be the string ‘buzz’.
        3) If the number in the original array is both a multiple of 3 and a multiple of 5, the
           corresponding element in the new array will be the string ‘fizzbuzz’.
        4) In all other cases, the element in the new array will have the same value as in the
           original array.
    """

    result_arr = StaticArray(arr.length())

    for num in range(arr.length()):
        if arr.get(num) % 3 == 0 and arr.get(num) % 5 == 0:
            result_arr[num] = 'fizzbuzz'
        elif arr.get(num) % 3 == 0:
            result_arr[num] = 'fizz'
        elif arr.get(num) % 5 == 0:
            result_arr[num] = 'buzz'
        else:
            result_arr[num] = arr[num]

    return result_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    This function receives a StaticArray and reverses the order of the elements in the array.
    """

    for index in range(arr.length() // 2):
        left = arr[index]
        right = arr[arr.length() - (index + 1)]
        arr[index] = right
        arr[arr.length() - (index + 1)] = left


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    This function receives two parameters - a StaticArray and an integer value (called steps).
    The function creates and returns a new StaticArray, which contains all the elements from
    the original array, but their position has shifted right or left steps number of times.
    """

    result_arr = StaticArray(arr.length())
    net_steps = steps % arr.length()

    for index in range(arr.length()):
        new_index = index + net_steps
        if new_index < arr.length():
            result_arr[new_index] = arr[index]
        else:
            result_arr[new_index - arr.length()] = arr[index]

    return result_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    This function receives the two integers start and end, and returns a StaticArray that
    contains all the consecutive integers between start and end (inclusive).
    """

    result_arr = StaticArray(abs(end-start) + 1)
    current_int = start

    if start < end:
        for index in range(result_arr.length()):
            result_arr[index] = current_int
            current_int += 1
    else:
        for index in range(result_arr.length()):
            result_arr[index] = current_int
            current_int -= 1

    return result_arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    This function receives a StaticArray and returns an integer that describes whether
    the array is sorted. The method will return:
        > 1 if the array is sorted in strictly ascending order
        > -1 if the list is sorted in strictly descending order
        > 0 otherwise.
    """

    if arr.length() == 1:
        return 1
    elif arr[0] < arr[1]:
        for index in range(arr.length() - 1):
            if arr[index] >= arr[index + 1]:
                return 0
        return 1
    elif arr[0] > arr[1]:
        for index in range(arr.length() - 1):
            if arr[index] <= arr[index + 1]:
                return 0
        return -1
    else:
        return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    This function receives a StaticArray that is sorted in order, either non-descending or
    non-ascending. The function will return, in this order, the mode (most-occurring value) of
    the array, and its frequency (how many times it appears).
    """
    mode = arr[0]
    mode_frequency = 1
    current = arr[0]
    current_frequency = 1

    for index in range(arr.length() - 1):
        if arr[index] == arr[index + 1]:
            current_frequency += 1
        else:
            current = arr[index + 1]
            current_frequency = 1
        if current_frequency > mode_frequency:
            mode = current
            mode_frequency = current_frequency

    return mode, mode_frequency


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray that is already in sorted order, either
    non-descending or non-ascending. The function will return a new StaticArray with all
    duplicate values removed.
    """
    new_length = 1

    for index in range(arr.length() - 1):
        if arr[index] is not arr[index + 1]:
            new_length += 1

    result_arr = StaticArray(new_length)
    result_arr[0] = arr[0]
    result_index = 1

    for index in range(arr.length() - 1):
        if arr[index] is not arr[index + 1]:
            result_arr[result_index] = arr[index + 1]
            result_index += 1

    return result_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    This function receives a StaticArray and returns a new StaticArray with the same
    content sorted in non-ascending order, using the count sort algorithm.
    """

    min, max = min_max(arr)

    # Initialize count array and set all values equal to 0
    count_arr = StaticArray(abs(max-min) + 1)
    for index in range(count_arr.length()):
        count_arr[index] = 0

    # Store instances of values within (min, max) range into count array
    for index in range(arr.length()):
        count_arr[(arr[index] - min)] += 1

    # Build new array with contents of input array in sorted in ascending order
    result_arr = StaticArray(arr.length())
    result_index = 0
    for index in range(count_arr.length()):
        for occurence in range(0, count_arr[index]):
            result_arr[result_index] = (index + min)
            result_index += 1
            occurence += 1

    reverse(result_arr)

    return result_arr


# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    This function receives three strings (source, s1, and s2) and returns a modified
    string that is the same length as source. The source string is processed one
    character at a time, and the output string is constructed according to these rules:
        1) If the character from the source string is present in s1 (any index), it should be
        replaced by the character at that same index in s2.
        2) Otherwise, if the character is:
            a) An uppercase letter -> replace with ' ' (a space)
            b) A lowercase letter -> replace with '#'
            c) A digit -> replace with '!'
            d) Anything else -> replace with '='
    """
    result_str = ""

    for index in range(len(source)):
        if source[index] in s1:
            s2_index = s1.find(source[index])
            new_char = s2[s2_index]
            result_str += new_char
        elif source[index].isupper():
            result_str += ' '
        elif source[index].islower():
            result_str += '#'
        elif source[index].isdigit():
            result_str += '!'
        else:
            result_str += '='

    return result_str


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['banana', 'apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [-972, -877, -664, -535, -534, -487, -432, -432, -276, -125, -53, -22, -19, 10, 184, 220, 504, 526, 574, 679,
         722, 748, 759, 800, 885],
        [988, 908, 887, 831, 390, 367, 331, 121, 61, 11, -172, -172, -261, -282, -293, -308, -349, -444, -453, -488, -689, -773, -955, -955, -955],
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')

    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
