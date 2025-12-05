# mark as true and process ingredients once we have passed the \n separator
processIngredients = False

# array of tuples (low, high)
ranges = []

res = 0

with open("./input.txt", "r") as file:
    
    for line in file:
        if line[0] == '\n':
            processIngredients = True
            continue
        
        if not processIngredients:
            nums = line.strip().split('-')
            ranges.append((int(nums[0]), int(nums[1])))
        else:
            for range in ranges:
                # if this is true it is in the range
                integer = int(line)
                if integer >= range[0] and integer <= range[1]:
                    res += 1
                    break
            
print(res)