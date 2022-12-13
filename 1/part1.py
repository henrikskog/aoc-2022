import sys

allSums = []

tempSum = 0
tempMax = 0
for line in sys.stdin.readlines():
    if line == '\n':
        if tempSum > tempMax:
            tempMax = tempSum
        tempSum = 0
        continue

    tempSum += int(line)

print(tempMax)