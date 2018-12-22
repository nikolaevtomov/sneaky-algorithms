#!/usr/bin/env python3


class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # Report swap
                print('Swapping child', self.heapList[i], 'at i =', i,
                      'with parent', self.heapList[i // 2], 'at i =', i // 2)
                # Swap
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
                print(self.heapList)
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        print('Adding', k, 'to heap list:', self.heapList)
        self.currentSize = self.currentSize + 1
        self.percolateUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolateDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                # Report swap
                print('Swapping parent', self.heapList[i], 'at i =', i,
                      'with child', self.heapList[mc], 'at i =', mc)
                # print('Swapping child', self.heapList[mc], 'at i =', mc,\
                # 'with parent', self.heapList[i], 'at i =', i)
                # Swap
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
                print(self.heapList)
            i = mc

    def delMin(self):
        returnValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percolateDown(1)
        return returnValue

    def buildHeap(self, aList):
        i = len(aList) // 2
        self.currentSize = len(aList)
        self.heapList = [0] + aList[:]
        print('Heap list:', self.heapList)
        while i > 0:
            self.percolateDown(i)
            i = i - 1


# Example 1 - adding items one at a time
myHeap = BinaryHeap()
aList = [9, 6, 5, 2, 3]
print('Example 1 - adding items one at a time')
print('List to build heap from:', aList)
print('Heap list:', myHeap.heapList)
print('-----------------------------------------')

for k in range(len(aList)):
    myHeap.insert(aList[k])
    print('-----------------------------------------')

print('Finished: heap is', myHeap.heapList)
print()

# Example 2 - "heapifying" an existing list
myHeap2 = BinaryHeap()
bList = [9, 6, 5, 2, 3]
print('Example 2 - heapifying an existing list')
print('List to heapify:', bList)

myHeap2.buildHeap(bList)
print('Finished')
