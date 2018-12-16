#!/usr/bin/env python3


def sortedHasDuplicate(numbers):
    sortedNumbers = sorted(numbers)
    lengthOfNumbers = len(sortedNumbers)
    duplicateItems = []
    duplicate = False

    for item in range(lengthOfNumbers):
        nextItem = item + 1

        if nextItem < lengthOfNumbers:
            if sortedNumbers[item] == sortedNumbers[nextItem]:
                duplicateItems.append(sortedNumbers[item])

    if len(duplicateItems) > 0:
        duplicate = True

    return duplicate


def hasDuplicate(numbers):
    duplicate = False
    duplicateItems = []

    for number in numbers:
            duplicateCount = 0

            for item in numbers:
                if(number == item):
                    duplicateCount = duplicateCount + 1

            duplicateItems.append(duplicateCount)
            duplicateCount = 0

    for item in duplicateItems:
        if item > 1:
            duplicate = True

    return duplicate


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


print('Tests for sortedHasDuplicate():')
print()
test('singleton', sortedHasDuplicate([4]), False)
test('sorted, no duplicate', sortedHasDuplicate([1, 2, 3]), False)
test('sorted, duplicate', sortedHasDuplicate([1, 2, 2, 3]), True)
print()
print('Tests for hasDuplicate() (must work for sorted lists too):')
print()
test('singleton', hasDuplicate([4]), False)
test('sorted, no duplicate', hasDuplicate([1, 2, 3]), False)
test('unsorted, no duplicate', hasDuplicate([3, 1, 2]), False)
test('sorted, duplicate', hasDuplicate([1, 2, 2, 3]), True)
test('unsorted, duplicate', hasDuplicate([2, 3, 2, 1]), True)

print()
print('Ran', ran, 'tests:', ran - failed, 'OK,', failed, 'FAILED')

if failed == 0:
    print('''All tests passed!''')
