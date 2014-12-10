import fibonacci

generator = fibonacci.generator()

current_number = 0
total = 0

while (current_number < 4000000):
    current_number = next(generator)
    if current_number % 2 == 0:
        total = total + current_number

print("Sum of even numbers: {}".format(total))
