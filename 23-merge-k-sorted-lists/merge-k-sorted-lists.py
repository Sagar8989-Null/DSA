# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        
        nodes = []

        for head in lists:
            curr = head

            while curr:
                nodes.append(curr)
                curr = curr.next
        
        if not nodes:
            return None

        nodes.sort(key=lambda node: node.val)

        for i in range(1,len(nodes)):
            nodes[i-1].next = nodes[i]

        nodes[-1].next = None

        return nodes[0]


