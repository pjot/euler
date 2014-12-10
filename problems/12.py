import prime

n = 1
limit = 500
while True:
    n = n + 1
    number = sum(range(n))
    factors = prime.get_all_factors(number)
    if len(factors) > limit:
        print("First triangle number with more than {} factors: {}".format(limit, number))
        exit()
