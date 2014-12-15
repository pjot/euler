import number

products = set()
for a in range(100):
    if '0' in str(a):
        continue
    for b in range(9876):
        if '0' in str(b):
            continue
        product = a * b
        if number.is_pandigital(str(product) + str(a) + str(b)):
            products.add(product)

print("Sum of products: {}".format(sum(products)))
