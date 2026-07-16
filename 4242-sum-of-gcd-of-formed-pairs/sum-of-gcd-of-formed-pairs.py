class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a,b):
            while b:
                a,b = b,a % b
            return a
        
        n = len(nums)
        Max = 0
        prefixGcd = [] 

        for i in range(n):
            Max = Max if Max > nums[i] else nums[i]
            prefixGcd.append(gcd(Max,nums[i]))
                    
        prefixGcd.sort()

        res=0
        i = 0 
        j = len(prefixGcd)-1

        while i<j:
            res += gcd(prefixGcd[i],prefixGcd[j]) 
            i+=1
            j-=1

        return res


        