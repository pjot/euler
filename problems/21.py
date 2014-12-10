import prime
divisor_sum = {}
for i in range(10000):
    factors = sum(i for i in prime.get_proper_factors(i))
    divisor_sum[i] = factors

total_sum = 0
for number in divisor_sum:
    div_sum = divisor_sum[number]
    if div_sum == number:
        continue
    try:
        if divisor_sum[div_sum] == number:
            total_sum = total_sum + number
    except KeyError:
        pass

print("Sum of amicable numbers: {}".format(total_sum))
