class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            h = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i) if i < len(heights) else None

        return max_area