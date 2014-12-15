import number

largest = 0
for n in range(1, 100000):
    for limit in range(1, 11):
        triple = [i * n for i in range(1, limit)]
        concat = "".join(str(i) for i in triple)
        if number.is_pandigital(concat):
            concat = int(concat)
            if concat > largest:
                largest = concat

print("Largest concatination: {}".format(largest))
