def is_palindrome_recursive(word, low_index, high_index):
    n = list(word)
    if word == '': return False
    if n[low_index] != n[high_index]: return False
    if low_index >= high_index: return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# word = 'araraaaaa'
# print(is_palindrome_recursive(word, 0, len(word) - 1))
