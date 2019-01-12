#!/usr/bin/env python3

import os
import time


def buildPrefixTable(target):
    prefixTable = [0] * len(target)
    q = 0

    for p in range(1, len(target)):
        while q > 0 and target[q] != target[p]:
            q = prefixTable[q - 1]

        if target[q] == target[p]:
            q = q + 1

        prefixTable[p] = q

    return prefixTable


def kmpSearch(searchString, target):
    n = len(searchString)
    m = len(target)
    prefixTable = buildPrefixTable(target)
    q = 0

    for i in range(n):
        while q > 0 and target[q] != searchString[i]:
            q = prefixTable[q - 1]

        if target[q] == searchString[i]:
            q = q + 1

        if q == m:
            return i - m + 1

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
print('kmpSearch() with target of ' + target1)
start = time.time()
print(kmpSearch(stringToSearch, target1))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('kmpSearch() with target of ' + target2)
start = time.time()
print(kmpSearch(stringToSearch, target2))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('kmpSearch() with target of ' + target3)
start = time.time()
print(kmpSearch(stringToSearch, target3))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()
