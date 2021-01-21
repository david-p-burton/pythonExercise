def getHeight(totalCoins):
    height = 0
    while(totalCoins > height):
        height += 1
        totalCoins = totalCoins - height
    return height

with open('C:/Users/David/Desktop/python/beginner/tricoinInput.txt') as f:
    total = f.readline()
    for x in range(int(total)):
        case = f.readline()
        caseHeight = getHeight(int(case))
        print("Test", x+1, "has a height of", caseHeight, ".")