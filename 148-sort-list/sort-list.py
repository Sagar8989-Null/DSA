# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 

        p1 = head
        arr = []

        while p1:
            arr.append(p1.val)
            p1 = p1.next

        arr.sort()
        
        dummy = ListNode()
        curr = dummy 

        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next