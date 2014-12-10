diagonal_limit = 1001
diagonal_length = 1
number_sum = 1
i = 1
side_skip = 2

while diagonal_length < diagonal_limit:
    for _ in range(4):
        for _ in range(side_skip):
            i += 1
        number_sum += i
    side_skip += 2
    diagonal_length += 2

print("Sum of diagonals: {}".format(number_sum))
