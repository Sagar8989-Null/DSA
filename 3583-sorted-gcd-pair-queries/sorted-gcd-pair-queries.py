class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

    
        exact = [0] * (mx + 1)

        for g in xrange(mx, 0, -1):
            cnt = 0
            for multiple in xrange(g, mx + 1, g):
                cnt += freq[multiple]

            exact[g] = cnt * (cnt - 1) // 2

            for multiple in xrange(g * 2, mx + 1, g):
                exact[g] -= exact[multiple]

     
        prefix = [0] * (mx + 1)
        for i in xrange(1, mx + 1):
            prefix[i] = prefix[i - 1] + exact[i]

        ans = []
        for q in queries:
            
            lo, hi = 0, mx
            while lo <= hi:
                mid = (lo + hi) // 2
                if prefix[mid] <= q:
                    lo = mid + 1
                else:
                    hi = mid - 1
            ans.append(lo)

        return ans