row = int(input())
column = int(input())

print((min(row + 1, 8) - max(row - 1, 1) + 1) * (min(column + 1, 8) - max(column - 1, 1) + 1) - 1)
