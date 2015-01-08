b = n = 1
while n < 1000000000000:
    b, n = 3*b + 2*n - 2, 4*b + 3*n - 3

print("Total balls: {}. Blue balls: {}".format(n, b))
