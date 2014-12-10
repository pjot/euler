import number

maximum = 0
current = 0
for i in range(1, 1000):
    cycle = number.get_fraction_cycle(i)
    if cycle > maximum:
        maximum = cycle
        current = i

print('Longest cycle of {} is for {}'.format(maximum, current))
