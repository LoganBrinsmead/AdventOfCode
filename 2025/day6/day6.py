data = []

with open("./input.txt", "r") as file:

    for line in file:
        line = line.strip().split()
        data.append(line)

res = 0
curData = 0
operation = '_'
operations = {
    '*': lambda x, y : x * y,
    '+':  lambda x, y : x + y
}

# start from the bottom to get the operation, then loop through the column to the top and apply the operation
for col in range(len(data[0])):
    for row in range(len(data) - 1, -1, -1):
        if row == len(data) - 1:
            operation = data[row][col]
            if operation == '*':
                curData += 1
        else:
            print(curData, data[row][col])
            curData = operations[operation](curData, int(data[row][col]))
    
    res += curData
    curData = 0

print(res)