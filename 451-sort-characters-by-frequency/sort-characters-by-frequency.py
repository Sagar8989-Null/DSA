class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        mp = {}
        
        for i in s:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        
        sortmp = sorted(mp.items(), key=lambda x: x[1], reverse=True)
    
        res = ''
        
        for i in sortmp:
            res += i[0]*i[1]
        
        return res   
        