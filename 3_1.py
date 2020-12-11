from functools import reduce

data_file = open("3_1.txt", "r")

data = data_file.read()
data = data.split("\n")

print(len(data[0]))

row_end = len(data)

jumps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_counts = []
for problem in jumps:
    right = problem[0]
    down = problem[1]
    j = int(0)
    row = 0
    trees = 0
    while row < row_end:
        for i in range(j, 31, right):
            if row < row_end:
                # print(f"Row: {row} Col: {i} Value:{data[row][i]}")
                if data[row][i] == "#":
                    trees += 1
                row += down
            else:
                break
            if i >= 30 - right:
                j = i + right - 31
    tree_counts.append(trees)
    print(trees)
answer = reduce(lambda x, y: x * y, tree_counts)
print(answer)
