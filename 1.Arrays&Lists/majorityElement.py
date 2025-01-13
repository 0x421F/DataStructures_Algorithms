questionList = [2, 2, 1, 1, 1, 2, 2]


# O(n) time complexity, O(n) space complexity
def majorityElement():
    numbers = {}
    result = 0
    maxNumber = 0

    for i in questionList:
        numbers[i] = 1 + numbers.get(i, 0)
        if numbers[i] > maxNumber:
            result = i
        maxNumber = max(maxNumber, numbers[i])
    return result


print(majorityElement())
