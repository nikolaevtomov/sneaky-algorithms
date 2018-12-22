#!/usr/bin/env python3


import random
import time


def selectionSort(aList):
    # print('Initial list =', aList)
    noOfSwaps = 0
    noOfAssignments = 0
    comparisons = 0
    start = time.time()
    for j in range(len(aList) - 1, 0, -1):
        maxPos = 0
        for i in range(1, j + 1):
            comparisons = comparisons + 1
            if aList[i] > aList[maxPos]:
                maxPos = i
        temp = aList[j]
        aList[j] = aList[maxPos]
        aList[maxPos] = temp
        noOfSwaps = noOfSwaps + 1
        noOfAssignments = noOfAssignments + 3
    elapsed = (time.time() - start)
    # print('Sorted list = ', aList)
    print('Comparisons =', comparisons)
    print('Swaps =', noOfSwaps)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')


randomList = []
for i in range(1, 4001):
    randomList.append(random.randrange(1, 4001))


print('TEST selectionSort()')
selectionSort(randomList)
print('----------------')

# print('randomList is now sorted', randomList)
# print('----------------')

print('TEST selectionSort() with sorted list')
selectionSort(randomList)
