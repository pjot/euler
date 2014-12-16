def is_bouncy(number):
    is_increasing = str(number) == "".join(sorted(str(number)))
    is_decreasing = str(number) == "".join(reversed(sorted(str(number))))
    return not(is_increasing or is_decreasing)

bouncy = 0
non_bouncy = 99
percentage = 99

i = 100
while bouncy * (100 - percentage) != non_bouncy * percentage:
    if is_bouncy(i):
        bouncy += 1
    else:
        non_bouncy += 1
    i += 1

print("Percentage {} reached at {}".format(percentage, i - 1))
