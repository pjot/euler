limit = 100

sum_of_squares = sum(i * i for i in range(limit + 1))
total = sum(i for i in range(limit + 1))
square_of_sum = total * total

print("Difference: {}".format(square_of_sum - sum_of_squares))
