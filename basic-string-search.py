#!/usr/bin/env python3
import os
import time


def basicStringSearch(searchString, target):
    searchIndex = 0

    for i in range(len(searchString) - len(target) + 1):
        targetIndex = 0

        while (targetIndex < len(target)) and target[targetIndex] == searchString[targetIndex + searchIndex]:
            targetIndex = targetIndex + 1

        if targetIndex == len(target):
            return searchIndex

        searchIndex = searchIndex + 1

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
print('basicStringSearch() with target of ' + target1)
start = time.time()
print(basicStringSearch(stringToSearch, target1))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('basicStringSearch() with target of ' + target2)
start = time.time()
print(basicStringSearch(stringToSearch, target2))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')

print()

print('----------------------------------------------------')
print('basicStringSearch() with target of ' + target3)
start = time.time()
print(basicStringSearch(stringToSearch, target3))
end = time.time()
print('Search completed in', "%.8f" % (end - start), 'seconds')
