#!/usr/bin/env python3


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def makeLists(tr):
    if tr is None:
        return []
    else:
        return [tr.getRootVal(), makeLists(tr.getLeftChild()), makeLists(tr.getRightChild())]


t1 = BinaryTree(9)

t1.insertLeft(26)
t1.insertRight(18)

t1.getLeftChild().insertLeft(44)
t1.getLeftChild().insertRight(77)
t1.getRightChild().insertLeft(31)
t1.getRightChild().insertRight(93)

t1.getLeftChild().getLeftChild().insertLeft(55)

print(makeLists(t1))


def nodeCount(tr):
    if tr is None:
        return 0
    else:
        return 1 + nodeCount(tr.getLeftChild()) + nodeCount(tr.getRightChild())


print('Node count:', nodeCount(t1))


def levelCount(tr):
    if tr is None:
        return 0
    else:
        return 1 + max(levelCount(tr.getLeftChild()), levelCount(tr.getRightChild()))


print('Level count:', levelCount(t1))
