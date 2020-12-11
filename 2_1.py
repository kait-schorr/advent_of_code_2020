import re

data_file = open("2_1.txt", "r")

data = data_file.read()
data = data.split("\n")

output = []
for line in data:
    output.append(
        [item for item in re.split(r"(\d*)-(\d*) (\w): (\w*)", line) if item != ""]
    )
final_count = 0
for password in output:
    min_count = int(password[0])
    max_count = int(password[1])
    letter = password[2]
    pw = password[3]
    count = pw.count(letter)
    if min_count <= count and count <= max_count:
        final_count += 1
print(final_count)

final_count = 0
for password in output:
    first = int(password[0])
    second = int(password[1])
    letter = password[2]
    pw = password[3]
    if (int(pw[first - 1] == letter) + int(pw[second - 1] == letter)) == 1:
        final_count += 1
print(final_count)
