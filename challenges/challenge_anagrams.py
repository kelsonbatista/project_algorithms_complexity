def validate(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    if len(first_string) != len(second_string):
        return False


def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1
    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = (
              string[delimiter], string[index]
            )
    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]
    return delimiter + 1


def is_anagram(first_string, second_string):
    s1 = list(first_string.lower())
    s2 = list(second_string.lower())
    validate(first_string, second_string)
    quick_sort(s1, 0, len(first_string) - 1)
    quick_sort(s2, 0, len(second_string) - 1)
    if s1 != s2:
        return False
    return True


# print(is_anagram('ReViVer', 'reVervi'))
