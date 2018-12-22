#!/usr/bin/env python3


class BinaryHeapSort:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
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
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def delMin(self):
        returnValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        # # Example 1
        # print('Pop root item', returnValue, 'and move last item to root')
        # print(self.heapList)
        # print('Percolate down')
        # print('-----------------------------------------------')
        self.percolateDown(1)
        # # Example 1
        # print(self.heapList)
        # print('    ^')
        return returnValue

    def buildHeap(self, aList):
        i = len(aList) // 2
        self.currentSize = len(aList)
        self.heapList = [0] + aList[:]
        while i > 0:
            self.percolateDown(i)
            i = i - 1
        return self.heapList[1:len(self.heapList)]

    def size(self):
        return self.currentSize


# # Example 1 heapsort in action
# aList = [1, 9, 5, 2, 14, 4, 8, 20, 7, 42]

# # First 'heapify' the list
# myHeap = BinaryHeapSort()
# myHeap.buildHeap(aList)

# # Create empty list to hold the results
# sortedList = []

# print('The list to be sorted:', aList)
# print('The heap:', myHeap.heapList)
# print()

# # While there are still items in the heap, pop the root and then reform the heap
# while myHeap.size() > 0:
#     item = myHeap.delMin()
#     sortedList.append(item)

# print('Finished')
# print('Sorted list:', sortedList)

# Example 2
myHeap = BinaryHeapSort()
myHeap.insert([5, 'Clean bathroom'])
myHeap.insert([3, 'Read email'])
myHeap.insert([4, 'Water plants'])
myHeap.insert([6, 'Phone dentist'])
myHeap.insert([1, 'Feed cat'])
myHeap.insert([2, 'Check weather forecast'])

print('To do list:')
while (myHeap.size() > 0):
    print(myHeap.delMin()[1])
