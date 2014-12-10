import prime

def get_prime_chain(a, b):
    n = 0
    while prime.is_prime(n**2 + a * n + b):
        n += 1
    return n

maximum = 0
product = 0
for a in range(-1000, 1000):
    for b in range(a, 1000):
        chain = get_prime_chain(a, b)
        if chain > maximum:
            maximum = chain
            product = a * b

print('Coefficient product: {}'.format(product))
