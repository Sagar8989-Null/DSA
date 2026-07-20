class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []

        for lis in grid:
            res.extend(lis)
            
        print(res)

        for i in range(k):
            val = res.pop()
            res.insert(0,val)

        print(res)

        final = []


        n = len(res)
        m = len(grid[0])
        i = 0 
        j = m

        while j <= n:
            print(i,j)
            final.append(res[i:j])
            i = j
            j += m 
            
        return final
                