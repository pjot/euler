letters = 0
for n in range(1, 1001):
    if n == 1000:
        letters = letters + len("onethousand")
        break
    if n > 99:
        letters = letters + len("hundred")
        if 299 < n < 400 or 699 < n < 900:
            letters = letters + len("three")
        if 399 < n < 600 or 899 < n:
            letters = letters + len("four")
        if n < 300 or 599 < n < 700:
            letters = letters + len("one")
        while n > 99:
            n = n - 100
        if not n == 0:
            letters = letters + len("and")
    if n > 9:
        if 69 < n < 80:
            letters = letters + len("seventy")
        if 19 < n < 40 or 79 < n:
            letters = letters + len("twenty")
        if 39 < n < 70:
            letters = letters + len("forty")
        if n == 17:
            letters = letters + len("seventeen")
            continue
        if n == 19 or n == 18 or n == 14 or n == 13:
            letters = letters + len("nineteen")
            continue
        if n == 16 or n == 15:
            letters = letters + len("sixteen")
            continue
        if n == 12 or n == 11:
            letters = letters + len("twelve")
            continue
        if n == 10:
            letters = letters + len("ten")
            continue
        while n > 9:
            n = n - 10
    if n == 8 or n == 7 or n == 3:
        letters = letters + len("eight")
    if n == 9 or n == 5 or n == 4:
        letters = letters + len("nine")
    if n == 6 or n == 2 or n == 1:
        letters = letters + len("ten")

print("Letter count: {}".format(letters))
