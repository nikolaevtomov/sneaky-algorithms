#!/usr/bin/env python3


import random
import time


def shortBubbleSort(aList):
    # print('Initial list =', aList)
    noOfSwaps = 0
    noOfAssignments = 0
    comparisons = 0
    hasSwapped = True
    passNum = len(aList) - 1
    start = time.time()
    while passNum > 0 and hasSwapped:
        hasSwapped = False
        for i in range(passNum):
            comparisons = comparisons + 1
            if aList[i] > aList[i + 1]:
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
                noOfSwaps = noOfSwaps + 1
                noOfAssignments = noOfAssignments + 3
                hasSwapped = True
        passNum = passNum - 1
    elapsed = (time.time() - start)
    # print('Sorted list = ', aList)
    print('Comparisons =', comparisons)
    print('Swaps =', noOfSwaps)
    print('Assignments =', noOfAssignments)
    print('Time taken =', elapsed, 'seconds')


randomList = []
for i in range(1, 4001):
    randomList.append(random.randrange(1, 4001))


print('shortBubbleSort()')
shortBubbleSort(randomList)
print('----------------')

# print('randomList is now sorted', randomList)
# print('----------------')

print('TEST shortBubbleSort() with sorted list')
shortBubbleSort(randomList)
