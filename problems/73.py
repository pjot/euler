THIRD = float(1) / 3
HALF = float(1) / 2

numbers = set()
for n in range(1, 12000 + 1):
    for nn in range(n/3, n/2 + 1):
        fraction = float(nn) / n
        if fraction in numbers:
            continue
        if THIRD < fraction < HALF:
            numbers.add(fraction)

print(len(numbers))
