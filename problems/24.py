import itertools

i = 0
for number in itertools.permutations('0123456789'):
    i += 1
    if i == 1000000:
        print("".join(item[0] for item in number))
        exit()
