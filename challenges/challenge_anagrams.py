def validate(first_string, second_string):
    if first_string == '':
        return False
    if second_string == '':
        return False
    if len(first_string) != len(second_string):
        return False


def is_anagram(first_string, second_string):
    s1 = list(first_string.lower())
    s2 = list(second_string.lower())
    response = validate(first_string, second_string)
    if response is False: return False
    for i in s1:
        if i not in s2 or s1.count(i) != s2.count(i):
            return False
    for i in s2:
        if i not in s1 or s1.count(i) != s2.count(i):
            return False  
    return True
