myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 1]


# 0(n) time complexity
# 0(n) space complexity
def contraindicate():
    hashSet = set()
    for i in myList:
        if i in hashSet:
            print("Duplicate")
            return True
        hashSet.add(i)
    return False


contraindicate()
