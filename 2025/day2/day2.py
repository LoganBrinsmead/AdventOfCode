
res = 0

with open("input.txt", "r") as inputFile:
    for line in inputFile:
        line = str(line)
        idsList = line.split(",")

        for id in idsList:
            id = str(id)
            id = id.split("-")
            firstId, lastId = int(id[0]), int(id[1])

            # lastId + 1 because it is inclusive
            for num in range(firstId, lastId + 1):

                window = ""
                strNum = str(num)

                # checking the current number for repeated sequences
                for i, c in enumerate(strNum):
                    if len(window) >= 1 and window[0] == c:
                        # loop through the rest of the window and the current number, checking for a duplicate
                        secondWindow = c
                        for j in range(i + 1, len(strNum)):
                            secondWindow += strNum[j]

                        if len(secondWindow) and secondWindow == window:
                            print("FOUND WINDOW! window: ", window, " ,secondWindow: ", secondWindow, ", strNum: ", strNum)
                            res += num
                            break
                    
                    # if len(strNum) >= i + 2 and strNum[i + 1] == c:
                    #     res += num
                    #     break

                    window += c
                    
                    



print(res)