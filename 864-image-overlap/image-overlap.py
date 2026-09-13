class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        
        ones1 = [(r, c) for r in range(len(img1)) for c in range(len(img1)) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(len(img2)) for c in range(len(img2)) if img2[r][c] == 1]
        
        shift_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
 
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] += 1
                max_overlap = max(max_overlap, shift_counts[shift])
                
        return max_overlap