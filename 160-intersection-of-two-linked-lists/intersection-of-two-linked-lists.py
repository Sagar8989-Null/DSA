# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        p1 = headA
        p2 = headB
        
        Seen = set()

        while p1:
            Seen.add(p1)
            p1 = p1.next

        while p2:
            if p2 in Seen:
                return p2
            
            Seen.add(p2)
            p2 = p2.next

        return None
