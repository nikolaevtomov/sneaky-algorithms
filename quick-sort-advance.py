#!/usr/bin/env python3

import os
import time
# import random


def quickSort(randomList):
    quickSortHelper(randomList, 0, len(randomList) - 1)


def quickSortHelper(randomList, first, last):
    if first < last:
        splitPoint = partition(randomList, first, last)
        quickSortHelper(randomList, first, splitPoint - 1)
        quickSortHelper(randomList, splitPoint + 1, last)


def partition(randomList, first, last):

    # Random value
    # pivotValue = random.choice(list(range(first, last + 1)))
    # temp = randomList[first]
    # randomList[first] = randomList[pivotValue]
    # randomList[pivotValue] = temp
    # Random value end

    # Median of three
    middle = (first + last) // 2
    items = sorted([(randomList[first], first), (randomList[middle], middle), (randomList[last], last)])
    (pivotValue, pivot) = items[1]
    temp = randomList[first]
    randomList[first] = randomList[pivot]
    randomList[pivot] = temp
    # Median of three end

    # First value
    # pivotValue = randomList[first]
    # First value ends

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


# fileName = 'list-unsorted-short.txt'
fileName = 'list-unsorted-long.txt'
# fileName = 'list-sorted-short.txt'
# fileName = 'list-sorted-long.txt'


# Helper get location function
def getLocation():
    return os.path.join(os.getcwd(), os.path.dirname(__file__))


# Helper read file function
def getNumbersFromFile(fileName):
    with open(os.path.join(getLocation(), 'dataset', fileName)) as f:
        randomList = [int(x) for x in f]
    f.close()

    return randomList


listOfItems = getNumbersFromFile(fileName)
print('INPUT = ', listOfItems[0:20])
start = time.time()
quickSort(listOfItems)
end = time.time()
print('OUTPUT = ', listOfItems[0:20])
print('List sorted in', (end - start), 'seconds')
