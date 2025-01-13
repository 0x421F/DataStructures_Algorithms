# Bit Manipulation
# Given an array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Solution:
def singleNumber():
    givenList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 8, 9]

    result = 0
    for i in givenList:
        result ^= i
    return result


print(singleNumber())
