data = []

with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = [c for c in line]
        data.append(line)


def part1():

    res = 0

    # we can track the columns that have beams in them using caching
    # stores index of column
    beamCols = set()
    beamCols.add(data[0].index('S'))

    for rowI, row in enumerate(data):
        for col in range(len(row)):
            if row[col] == "^" and col in beamCols:
                beamCols.remove(col)
                res += 1
                if col - 1 >= 0 and data[rowI][col] != '|':
                    data[rowI][col - 1] = '|'
                    beamCols.add(col - 1)
                if col + 1 < len(row) and data[rowI][col + 1] != '|':
                    beamCols.add(col + 1)
                    data[rowI][col + 1] = '|'
                
    return res

def part2():

    # col index: number of timelines currently running through that column
    beamCols = {data[0].index('S'): 1}

    for rowI, row in enumerate(data):
        for col in range(len(row)):
            if row[col] == "^" and col in beamCols:
                print(beamCols)
                prev = col - 1
                next = col + 1
                if prev >= 0:
                    if prev in beamCols:
                        beamCols[prev] += beamCols[col]
                    else:
                        beamCols[prev] = beamCols[col]
                if next < len(row):
                    if next in beamCols:
                        beamCols[next] += beamCols[col]
                    else:
                        beamCols[next] = beamCols[col]

                del beamCols[col]

    
    return sum(beamCols.values())

print(part2())