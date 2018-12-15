#!/usr/bin/env python3

import random
import time
from copy import copy


def quickSort(randomList):
    quickSortHelper(randomList, 0, len(randomList) - 1)


def quickSortHelper(randomList, first, last):
    if first < last:
        splitPoint = partition(randomList, first, last)
        quickSortHelper(randomList, first, splitPoint - 1)
        quickSortHelper(randomList, splitPoint + 1, last)


def partition(randomList, first, last):
    pivotValue = randomList[first]
    leftMark = first + 1
    rightMark = last
    done = False

    while not done:
        while leftMark <= rightMark and randomList[leftMark] <= pivotValue:
            leftMark = leftMark + 1

        while randomList[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:
            temp = randomList[leftMark]
            randomList[leftMark] = randomList[rightMark]
            randomList[rightMark] = temp

    temp = randomList[first]
    randomList[first] = randomList[rightMark]
    randomList[rightMark] = temp

    return rightMark


# Unsorted list of random integers
listOfItems = []
for i in range(1, 4001):
    listOfItems.append(random.randrange(1, 4001))


start = time.time()
quickSort(copy(listOfItems))
end = time.time()
print('List sorted in', (end - start), 'seconds')
