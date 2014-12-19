import math
limit = 1000000

class Fraction:
    n = 1
    d = 1
    value = 1

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def set_value(self):
        self.value = self.n / self.d

    def get_name(self):
        return "{}/{}".format(self.n, self.d)

fractions = []
for i in range(1, limit + 1):
    j = math.floor(i * 3 / 7)
    f = Fraction(j, i)
    f.set_value()
    fractions.append(f)

fractions.sort(key=lambda f: f.value)

for i, f in enumerate(fractions):
    if fractions[i + 1].get_name() == "3/7":
        print("Number to the left: {}".format(f.get_name()))
        exit()
