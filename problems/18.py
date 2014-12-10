pyramid = []
with open("problems/18.txt") as f:
    for line in f:
        pyramid.append([int(i) for i in line.rstrip().split(" ")])

last_line = pyramid.pop()
while True:
    next_line = pyramid.pop()
    for i in range(len(next_line)):
        if last_line[i] > last_line[i + 1]:
            next_line[i] = next_line[i] + last_line[i]
        else:
            next_line[i] = next_line[i] + last_line[i + 1]
    last_line = next_line
    if len(pyramid) == 0:
        break

print("Total for largest path: {}".format(last_line.pop()))
