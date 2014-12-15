def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse(n)

def length(n):
    return len(str(n))

def get_fraction_cycle(n):
    for digits in range(1,1000):
        if (10 ** digits - 1) % n == 0:
            return digits
    return 0

def is_pandigital(number):
    if '0' in number:
        return False
    return len(number) == 9 and '123456789'.strip(number) == ""

def get_subdigits(number, first, second, third):
    s = str(number)
    return int(s[first - 1] + s[second - 1] + s[third - 1])
