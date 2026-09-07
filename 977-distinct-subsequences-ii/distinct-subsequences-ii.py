class Solution:
    def distinctSubseqII(self, s: str) -> int:

        MOD = 1_000_000_007
        
        ends_in = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            
            ends_in[idx] = (sum(ends_in) + 1) % MOD
        
        return sum(ends_in) % MOD
