# mark as true and process ingredients once we have passed the \n separator
processIngredients = False

# array of tuples (low, high)
ranges = []

res = 0
partTwoRes = 0

with open("./input.txt", "r") as file:
    
    for line in file:
        if line[0] == '\n':
            processIngredients = True
            continue
        
        if not processIngredients:
            nums = line.strip().split('-')
            ranges.append([int(nums[0]), int(nums[1])])
        else:
            for range in ranges:
                # if this is true it is in the range
                integer = int(line)
                if integer >= range[0] and integer <= range[1]:
                    res += 1
                    break
        
        # merge overlapping intervals
        ranges.sort()
        filteredRanges = [ranges[0]]
        for start, end in ranges[1:]:
            #  get the ending value of the last sorted interval
             lastEnd = filteredRanges[-1][1]

            #  if true, this means that the intervals are overlapping, so we just take the max ending value. otherwise they don't overlap, so just append.
             if start <= lastEnd:
                  filteredRanges[-1][1] = max(lastEnd, end)
             else:
                  filteredRanges.append([start, end])
                 

    for range in filteredRanges:    
            partTwoRes += (range[1] - range[0]) + 1
            
print(res, partTwoRes)