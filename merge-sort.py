#!/usr/bin/env python3

import random
import time
from copy import copy


def mergeSort(randomList):
    if len(randomList) > 1:
        midPivotd = len(randomList) // 2

        leftPartition = randomList[:midPivotd]
        rightPartition = randomList[midPivotd:]

        mergeSort(leftPartition)
        mergeSort(rightPartition)

        i = 0
        j = 0
        k = 0

        while i < len(leftPartition) and j < len(rightPartition):
            if leftPartition[i] < rightPartition[j]:
                randomList[k] = leftPartition[i]
                i = i + 1
            else:
                randomList[k] = rightPartition[j]
                j = j + 1
            k = k + 1

        while i < len(leftPartition):
            randomList[k] = leftPartition[i]
            i = i + 1
            k = k + 1

        while j < len(rightPartition):
            randomList[k] = rightPartition[j]
            j = j + 1
            k = k + 1


# Unsorted list of random integers
listOfItems = []
for i in range(1, 4001):
    listOfItems.append(random.randrange(1, 4001))


start = time.time()
mergeSort(copy(listOfItems))
end = time.time()
print('List sorted in', (end - start), 'seconds')
