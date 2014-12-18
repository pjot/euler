import math

i = 1
highest_line = 0
highest_value = 0
with open("problems/99.txt") as f:
    for line in f:
        number, exponent = (int(i) for i in line.rstrip().split(","))
        value = exponent * math.log(number)
        if value > highest_value:
            highest_value = value
            highest_line = i
        i += 1

print("Line number: {}".format(highest_line))
