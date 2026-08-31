class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        criticals = []

        p3 = head
        p2 = head.next
        p1 = head.next.next
        dist = 2

        while p1:

            if p2.val > p1.val and p2.val > p3.val:
                criticals.append(dist)

            if p2.val < p1.val and p2.val < p3.val:
                criticals.append(dist)

            p3 = p2
            p2 = p1
            p1 = p1.next
            dist += 1

        if len(criticals) < 2:
            return [-1, -1]

        maxDistance = criticals[-1] - criticals[0]

        minDistance = float('inf')

        for i in range(1, len(criticals)):
            distance = criticals[i] - criticals[i - 1]
            minDistance = min(minDistance, distance)

        return [minDistance, maxDistance]

