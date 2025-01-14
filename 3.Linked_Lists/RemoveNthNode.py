# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        leftPointer = head
        rightPointer = head

        while n > 0 and rightPointer.next:
            rightPointer = rightPointer.next
            n -= 1

        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        if leftPointer == head and not rightPointer:
            return head.next
        
        leftPointer.next = leftPointer.next.next

        return head