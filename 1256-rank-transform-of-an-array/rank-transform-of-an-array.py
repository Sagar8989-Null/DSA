class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
    
        Dict = {}
        for i,j in enumerate(sorted(set(arr))):
            Dict[j] = i

        for i in range(len(arr)):
            arr[i] = Dict[arr[i]]+1

        return arr
