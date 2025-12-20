"""
row, col
1, 11
5, 2

10 * 5 = 50
10 0's in a row, 5 0's in a column between these two points

11 - 2 + 1 = 10
5 - 1 + 1 = 5

10 * 5 = 50
"""

data = []

with open ("./input.txt", "r") as file:

    for line in file:
        coordinates = line.strip().split(",")
        coordinates = [int(i) for i in coordinates]
        data.append(tuple(coordinates))

def findDistance(coord1, coord2):
    colDistance = abs(coord1[1] - coord2[1] + 1)
    rowDistance = abs(coord1[0] - coord2[0] + 1)

    return colDistance * rowDistance


def part1():
    res = 0

    for i in range(len(data)):
        for j in range(i, len(data)):
            res = max(findDistance(data[i], data[j]), res)


    return res
