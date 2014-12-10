import prime

total = 0
limit = 2000000
generator = prime.Prime()
current_prime = generator.next()

while current_prime < limit:
    total = total + current_prime
    current_prime = generator.next()

print("Sum of all primes below {}: {}".format(limit, total))
