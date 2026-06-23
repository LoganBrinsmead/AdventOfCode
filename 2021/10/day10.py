# open the file
data = []

with open ("./input.txt", "r") as file:

    for line in file:
        line = str(line)
        line = line.strip()
        data.append(line)

stack = []
scores = []

# as you go along, just keep appending to the stack
# if it is a closing parenthesis but doesn't match the top of the stack, we know it is an illegal parenthesis and we can add to our res
res = 0

scoreMap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

partTwoScoreMap = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4

}

matchMap = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

# part one
for line in data:
    for c in line:
        # it is an opener, just append
        if c not in matchMap:
            stack.append(c)
        else:
            # is the top of the stack the proper opener? if not, add to res.
            if stack[-1] != matchMap[c]:
                res += scoreMap[c]
            
            stack.pop()
        
    
    stack = []

# part two
for line in data:
    for c in line:
        if c in matchMap and stack[-1] in partTwoScoreMap:
            stack.pop()
        elif c in partTwoScoreMap:
            stack.append(c)
    
    print(stack)
    lineTotal = 0
    for i in range(len(stack)):
        lineTotal *= 5
        lineTotal += partTwoScoreMap[stack[i]]
    
    scores.append(lineTotal)

    
    stack = []


scores.sort()

partTwoRes = scores[len(scores) // 2]

print(partTwoRes)