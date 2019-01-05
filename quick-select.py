#!/usr/bin/env python3


def quickSelect(k, aList):
    """Searches for the k-th smallest items in the list """

    if len(aList) == 1:
        return aList[0]

    pivotValue = aList[0]
    leftPart = []
    rightPart = []

    for item in aList[1:]:
        if item < pivotValue:
            leftPart.append(item)
        else:
            rightPart.append(item)

    if len(leftPart) >= k:
        return quickSelect(k, leftPart)
    elif len(leftPart) == k - 1:
        return pivotValue
    else:
        return quickSelect(k - len(leftPart) - 1, rightPart)


theList = [2, 36, 5, 21, 8, 13, 11, 20, 4, 1]
print(quickSelect(6, theList))
