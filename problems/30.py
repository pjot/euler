total = 0
for number in range(2, 999999):
    current_sum = sum(int(i)**5 for i in str(number))
    if current_sum == number:
        total += number

print('Sum of numbers: {}'.format(total))
