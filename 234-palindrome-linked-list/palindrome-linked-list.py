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
        
        S = []

        while head:
            S.append(str(head.val))
            head = head.next  

        S = "".join(S)

        return S == S[::-1]
    