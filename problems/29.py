ceiling = 101
powers = set()

for a in range(2, ceiling):
    for b in range(2, ceiling):
        powers.add(a**b)

print("Distinct powers: {}".format(len(powers)))
