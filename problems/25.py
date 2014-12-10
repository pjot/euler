import fibonacci
import number

generator = fibonacci.generator()

current_number = 0
i = 1
while (number.length(current_number) < 1000):
    current_number = next(generator)
    i = i + 1

print("First Fibonacci number with 1000 digit: {}".format(i))
