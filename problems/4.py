import number

def get_palindromes(n):
    for a in range(n):
        for b in range(n):
            if a >= b and number.is_palindrome(a * b):
                yield a * b

highest = 0
for num in get_palindromes(1000):
    if num > highest:
        highest = num

print("Highest palindrome: {}".format(highest))
