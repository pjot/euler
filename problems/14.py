chains = {}

def count_chain(n, chains):
    i = 0
    while not n == 1:
        if n in chains:
            i = i + chains[n]
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        i = i + 1
    return i

highest = 0
number = 0
for i in range(1, 1000000):
    chains[i] = count_chain(i, chains)
    if chains[i] > highest:
        number = i
        highest = chains[i]

print("Longest chain: {}".format(number))
