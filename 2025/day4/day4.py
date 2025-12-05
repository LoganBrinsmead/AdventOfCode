# the 8 adjacent positions the rolls can be in
# (row, col)
directions = [
    (0, 1),
    (0, -1),
    (-1, -1),
    (-1, 0), 
    (-1, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

matrix = []
row = []
with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        row = [c for c in line]
        matrix.append(row)

res = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):

        # don't count empty cells
        if matrix[row][col] == '.':
            continue

        countAdjacent = 0
        for dir in directions:
            dr, dc = dir[0], dir[1]
            curDirection = (row + dr, col + dc)
            if (
            curDirection[0] < 0 or
            curDirection[0] >= len(matrix) or
            curDirection[1] < 0 or
            curDirection[1] >= len(matrix[row])):
                continue

            if matrix[curDirection[0]][curDirection[1]] == '@':
                countAdjacent += 1
            
        
        if countAdjacent < 4:
            res += 1
        

print(res)