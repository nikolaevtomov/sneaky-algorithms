#!/usr/bin/env python3

import os
import time


def buildShiftTable(target, alphabet):
    shiftTable = {}

    for char in alphabet:
        shiftTable[char] = len(target) + 1

    for i in range(len(target)):
        character = target[i]
        shift = len(target) - i
        shiftTable[character] = shift

    return shiftTable


def quickSearch(searchString, target, alphabet):
    shiftTable = buildShiftTable(target, alphabet)
    searchIndex = 0

    while searchIndex + len(target) <= len(searchString):
        targetIndex = 0

        while targetIndex < len(target) and target[targetIndex] == searchString[searchIndex + targetIndex]:
            targetIndex = targetIndex + 1

        if targetIndex == len(target):
            return searchIndex

        if searchIndex + len(target) < len(searchString):
            next = searchString[searchIndex + len(target)]
            shift = shiftTable[next]
            searchIndex = searchIndex + shift

        else:
            return -1

    return -1


# Helper get location function
def getLocation():
    return os.path.join(os.getcwd(), os.path.dirname(__file__))


def getBigString():
    with open(os.path.join(getLocation(), 'dataset', 'searchData.txt'), 'r') as myfile:
        bigString = myfile.read()
    return bigString


theAlphabet = {'G', 'A', 'C', 'T'}

stringToSearch = getBigString()

target1 = 'CGTCCA'
target2 = 'TATATA'
target3 = 'CTCTATGTTTAAAGTTCGA'


print('----------------------------------------------------')
print('quickSearch() with target of ' + target1)
start = time.time()
print(quickSearch(stringToSearch, target1, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('quickSearch() with target of ' + target3)
start = time.time()
print(quickSearch(stringToSearch, target3, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('quickSearch() with target of ' + target3)
start = time.time()
print(quickSearch(stringToSearch, target3, theAlphabet))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')
