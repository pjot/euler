import number
import itertools

def has_property(n):
    if number.get_subdigits(n, 2, 3, 4) % 2 != 0:
        return False
    if number.get_subdigits(n, 3, 4, 5) % 3 != 0:
        return False
    if number.get_subdigits(n, 4, 5, 6) % 5 != 0:
        return False
    if number.get_subdigits(n, 5, 6, 7) % 7 != 0:
        return False
    if number.get_subdigits(n, 6, 7, 8) % 11 != 0:
        return False
    if number.get_subdigits(n, 7, 8, 9) % 13 != 0:
        return False
    if number.get_subdigits(n, 8, 9, 10) % 17 != 0:
        return False
    return True

sum = 0
for n in itertools.permutations('0123456789'):
    a = "".join(n)
    if has_property(a):
        sum += int(a)

print("Sum of pandigital numbers: {}".format(sum))

