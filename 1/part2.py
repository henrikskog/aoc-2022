import sys

allSums = []

tempSum = 0
tempMax = 0
for line in sys.stdin.readlines():
    print(line)
    if line == '\n':
        allSums.append(tempSum)
        tempSum = 0
        continue

    tempSum += int(line)

print(sum(sorted(allSums)[-3:]))

