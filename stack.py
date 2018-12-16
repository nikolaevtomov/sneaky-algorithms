#!/usr/bin/env python3


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Create a stack
myStack = Stack()

# Push items on to the stack
myStack.push(43)
myStack.push(71)
myStack.push(16)
myStack.push(27)


def displayStack(aStack):
    stackCopy = Stack()
    for x in range(aStack.size()):
        stackItem = aStack.pop()
        print('    ', stackItem)
        stackCopy.push(stackItem)
    print('=============')
    for y in range(stackCopy.size()):
        stackItem = stackCopy.pop()
        aStack.push(stackItem)


# Call displayStack()
displayStack(myStack)
