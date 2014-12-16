import prime
limit = 1000000

primes = [i for i in prime.get_primes_below(limit)]
longest_sum = 0
longest_prime = 0
for i in range(3):
    sum = 0
    count = 0
    while sum < limit:
        count += 1
        try:
            sum += primes[i + count]
        except IndexError:
            break
        if count > 1 and sum in primes:
            if count > longest_sum:
                longest_sum = count
                longest_prime = sum
print("Longest prime: {}".format(longest_prime))
