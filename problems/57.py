fractions = 0
n = 7
d = 5
for i in range(2, 1000):
    n, d = 2 * d + n, d + n
    if len(str(n)) > len(str(d)):
        fractions += 1
print("Fractions: {}".format(fractions))

