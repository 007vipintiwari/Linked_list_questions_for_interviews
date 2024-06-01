"""
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list,
reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextptr = head
        curr = head
        previous = None

        while nextptr != None:
            nextptr = nextptr.next
            curr.next = previous
            previous = curr
            curr = nextptr

        return previous
