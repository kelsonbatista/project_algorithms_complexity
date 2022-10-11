def is_palindrome_iterative(word):
    n = list(word)
    size = len(word)
    if word == '': return False
    for i in range(size - 1):
        if n[i] != n[size - i - 1]: return False
        if i >= size - i: return True
    return True


# word = 'revivir'
# print(is_palindrome_iterative(word))
