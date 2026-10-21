class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        p1 = 0
        p2 = 0
        formed = 0
        required = len(need)

        sol = ""
        min_len = float("inf")

        while p2 < len(s):
            c = s[p2]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            while formed == required:
                if p2 - p1 + 1 < min_len:
                    min_len = p2 - p1 + 1
                    sol = s[p1:p2 + 1]

                left_char = s[p1]
                window[left_char] -= 1

                if (left_char in need and
                        window[left_char] < need[left_char]):
                    formed -= 1

                p1 += 1

            p2 += 1

        return sol
                    