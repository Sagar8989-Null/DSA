# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        val = []

        while head:
            val.append(str(head.val))
            head = head.next  

        S = "".join(val)

        return S == S[::-1]
    