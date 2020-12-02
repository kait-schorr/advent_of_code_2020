import numpy

data_file = open("1_1.txt", "r")

data = data_file.read()
data = data.split("\n")
data = list(map(lambda x: int(x), data))
data.sort()

# Part One
for num in data:
    if (2020 - num) in data:
        print(num * (2020 - num))
        break

# Part Two
# Brute Force (Gross)

for a in data:
    for b in data:
        for c in data:
            if a + b + c == 2020:
                print(a * b * c)

