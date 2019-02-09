#!/usr/bin/env python3


def chopIntoPairs(aNumber):
    numString = str(aNumber)
    pairs = []
    for i in range(0, len(numString), 2):
        pairs.append(int(numString[i: i + 2]))
    return pairs


def getMiddle(aNumber):
    numString = str(aNumber)
    midPoint = len(numString) // 2
    if (len(numString) % 2) == 0:
        middle = int(numString[midPoint - 1:midPoint + 1])
    else:
        middle = int(numString[midPoint])
    return middle


def hashFold(aNumber, tableSize):
    numList = chopIntoPairs(aNumber)
    total = 0
    for item in numList:
        total = total + item
    return total % tableSize


def hashMidSquare(aNumber, tableSize):
    numberSquared = aNumber * aNumber
    midSequence = getMiddle(numberSquared)
    hashNumber = midSequence % tableSize
    return hashNumber


print(hashFold(1459862903, 23))
print(hashMidSquare(1459862903, 23))
