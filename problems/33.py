def get_common_digits(a, b):
    if a == b:
        return []
    if str(a) == str(b)[::-1]:
        return [a % 10, b % 10]
    for n in range(1, 10):
        if not(str(n) in str(a) and str(n) in str(b)):
            continue
        first = str(a).index(str(n)) == 0 and str(b).index(str(n)) == 1
        second = str(b).index(str(n)) == 0 and str(a).index(str(n)) == 1
        if first or second:
            return [n]
    return []

def find_lowest_form(a, b):
    smallest = min(a, b)
    for i in range(2, smallest):
        while is_divisible(a, i) and is_divisible(b, i):
            a = a / i
            b = b / i
    return [int(a), int(b)]

def is_divisible(a, b):
    return a % b == 0

numerators = 1
denominators = 1
for a in range(10, 100):
    for b in range (10, a):
        for digit in get_common_digits(a, b):
            new_a = int(str(a).replace(str(digit), '', 1))
            new_b = int(str(b).replace(str(digit), '', 1))
            if new_a == 0:
                continue
            if b / a == new_b / new_a:
                numerators = numerators * new_b
                denominators = denominators * new_a

print("Product of denominators: {}".format(find_lowest_form(numerators, denominators)[1]))
