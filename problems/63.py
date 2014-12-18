integers = 0
for n in range(1, 25):
    i = 1
    if n > 1:
        i += 1
    while True:
        power = i**n
        length = len(str(power))
        if length == n:
            integers += 1
        if length > n:
            break
        i += 1
print("Integers: {}".format(integers))
