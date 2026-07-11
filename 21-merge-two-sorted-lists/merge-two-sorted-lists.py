# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        res = []

        while list1:
            res.append(list1.val)
            list1 = list1.next

        while list2:
            res.append(list2.val)
            list2 = list2.next

        res.sort()

        if not res:
            return None

        head = ListNode(res[0])
        node = head

        for i in range(1, len(res)):
            node.next = ListNode(res[i])
            node = node.next

        return head