#!/usr/bin/env python3


class Set:
    def __init__(self):
        self.items = []

    def has(self, item):
        return item in self.items

    def put(self, item):
        assert not (item in self.items)
        self.items.append(item)

    def size(self):
        return len(self.items)

    def take(self, item):

        index = 0
        while index < self.size():
            if self.items[index] == item:
                self.items.pop(index)
            else:
                index += 1

    def common(self, other):
        items = Set()

        for item in self.items:
            if other.has(item):
                items.put(item)

        return items


# TESTS
failed = 0
ran = 0


def test(name, actual, expected):
    global ran, failed

    if actual == expected:
        print(name, 'OK')
    else:
        print(name, 'FAILED: got', actual, 'instead of', expected)
        failed += 1
    ran += 1


even = Set()
even.put(0)
even.put(2)
even.put(4)
even.put(6)

squares = Set()
squares.put(0)
squares.put(1)
squares.put(4)
squares.put(9)

even_squares = even.common(squares)
test('even squares size', even_squares.size(), 2)
test('0 is an even square', even_squares.has(0), True)
test('4 is an even square', even_squares.has(4), True)
test('2 is even, not square', even_squares.has(2), False)

square_evens = squares.common(even)
test('same size', even_squares.size() == square_evens.size(), True)
for n in range(10):
    test('has ' + str(n), even_squares.has(n) == square_evens.has(n), True)

odd = Set()
odd.put(1)
odd.put(3)

test('no common numbers', odd.common(even).size(), 0)

print()
print('All tests run:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''All tests passed!''')
