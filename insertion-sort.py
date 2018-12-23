#!/usr/bin/env python3


import random
import time


def insertionSort(aList):
    # print('Initial list =', aList)
    shifts = 0
    noOfAssignments = 0
    comparisons = 0
    start = time.time()
    for i in range(1, len(aList)):
        currentValue = aList[i]
        noOfAssignments = noOfAssignments + 1
        position = i
        entered = False
        while position > 0 and aList[position - 1] > currentValue:
            entered = True
            comparisons = comparisons + 1
            aList[position] = aList[position - 1]
            shifts = shifts + 1
            noOfAssignments = noOfAssignments + 1
            position = position - 1
        aList[position] = currentValue
        noOfAssignments = noOfAssignments + 1
        if not entered:
            comparisons = comparisons + 1
    elapsed = time.time() - start
    # print('Sorted list = ', aList)
    print('Comparisons =', comparisons)
    print('Shifts =', shifts)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')


randomList = []
for i in range(1, 4001):
    randomList.append(random.randrange(1, 4001))


print('insertionSort()')
insertionSort(randomList)
print('----------------')

# print('randomList is now sorted', randomList)
# print('----------------')

print('insertionSort() with sosted list')
insertionSort(randomList)
