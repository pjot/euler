def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse(n)

def length(n):
    return len(str(n))
