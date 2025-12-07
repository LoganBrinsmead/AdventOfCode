
prep = []

with open("./input.txt", "r") as file:

    for line in file:
        line = line.replace("\n", "")
        line = list(line)
        prep.append(line)

data = []
colCount = len(prep[0]) - 1
curValue = ''
curRow = []

# if current symbol is an operation, append current values to matrix
while colCount > -1:
    if curValue.isdigit():
        curRow.append(curValue)
    curValue = ''

    for row in range(len(prep)):
        if prep[row][colCount] == '*' or prep[row][colCount] == '+':
            if curValue.isdigit():
                curRow.append(curValue)
                curValue = ''

            curRow.append(prep[row][colCount])
            data.append(curRow)
            curRow = []
        elif prep[row][colCount].isdigit():
            curValue += prep[row][colCount]
    
    colCount -= 1

res = 0
curData = 0
operation = '_'
operations = {
    '*': lambda x, y : x * y,
    '+':  lambda x, y : x + y
}

for row in data:
    operation = row[len(row) - 1]
    if operation == '*':
        curData = 1


    for i in range(len(row) - 1):
        curData = operations[operation](curData, int(row[i]))
    
    res += curData
    curData = 0

print(res)