def is_pandigital(number):
    if '0' in number:
        return False
    return len(number) == 9 and '123456789'.strip(number) == ""

products = set()
for a in range(100):
    if '0' in str(a):
        continue
    for b in range(9876):
        if '0' in str(b):
            continue
        product = a * b
        if is_pandigital(str(product) + str(a) + str(b)):
            products.add(product)

print("Sum of products: {}".format(sum(products)))
