import fibonacci
import number

def is_pandigital(n):
    second = number.is_pandigital(str(n % 1000000000))

    if not second:
        return False

    while n > 1000000000000000:
        n = n // 1000000
    while n > 1000000000:
        n = n // 10

    return number.is_pandigital(str(n))

generator = fibonacci.generator()
i = 2
while True:
    if is_pandigital(next(generator)):
        break
    i = i + 1

print("First Fibonacci number with pandigital start and end: {}".format(i))
