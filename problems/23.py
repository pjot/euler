import prime

abundant_numbers = []
for i in range(1, 28124):
    digit_sum = sum(prime.get_proper_factors(i))
    if 28124 > digit_sum > i:
        abundant_numbers.append(i)

sums = set()
for a in abundant_numbers:
    for b in abundant_numbers:
        if a + b < 28124:
            sums.add(a + b)

total_sum = 0
for i in range(1, 28124):
    if not i in sums:
        total_sum = total_sum + i

print("Total sum: {}".format(total_sum))
