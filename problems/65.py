from fractions import Fraction

first = 2
limit = 100

def get_c(n):
    if n % 3 == 1 or n % 3 == 0:
        return 1
    return int(2 * (n + 1) / 3)

representation = []
for i in range(1, limit):
    representation.append(get_c(i))

last_number = 0
for place in range(1, limit):
    e = Fraction(0)
    part = representation[0:place]
    for n in reversed(part):
        e = n + e
        e = 1 / e
    last_number = e + first

digit_sum = sum(int(i) for i in str(last_number.numerator))
print("Digit sum:", digit_sum)
