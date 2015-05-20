replacements = {
    'DCD': 'CM',
    'LXL': 'XC',
    'VIV': 'IX',
    'CCCC' : 'CD',
    'XXXX' : 'XL',
    'IIII' : 'IV',
}

def minimize(number):
    replaced = number

    for old, new in replacements.items():
        replaced = replaced.replace(old, new)

    if replaced == number:
        return number

    return minimize(replaced)

less = 0
with open("problems/89.txt") as f:
    for line in f:
        line = line.rstrip()
        difference = len(line) - len(minimize(line))
        less += difference

print(less)
