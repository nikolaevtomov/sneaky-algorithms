#!/usr/bin/env python3


import random
import time


def bubbleSort(aList):
    # print('Initial list =', aList)
    noOfSwaps = 0
    noOfAssignments = 0
    comparisons = 0
    start = time.time()
    for passNum in range(len(aList) - 1, 0, -1):
        for i in range(passNum):
            comparisons = comparisons + 1
            if aList[i] > aList[i + 1]:
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
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


print('bubbleSort()')
bubbleSort(randomList)
print('----------------')

# print('randomList is now sorted', randomList)
# print('----------------')

print('TEST bubbleSort() with sorted list')
bubbleSort(randomList)
