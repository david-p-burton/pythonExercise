def intCast(n):
    return int(n)

with open('C:/Users/David/Desktop/python/addTwoNumbersInput.txt') as f:
    total = f.readline()
    for x in range(int(total)):
        line = f.readline().split()
        line1 = [*map(intCast, line)]
        print(sum(line1))