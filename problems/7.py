import prime

limit = 10001
generator = prime.Prime()
for i in range(limit - 1):
    generator.next()

print("The {}th prime is: {}".format(limit, generator.next()))
