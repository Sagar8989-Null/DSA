class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = 0
        mid = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                mid = chr(ord('a') + i)

        if odd > 1:
            return ""

        half = [x // 2 for x in cnt]
        half_len = n // 2

        left = []

        def feasible() -> bool:
            candidate = left[:]

            for c in range(25, -1, -1):
                candidate.extend([chr(ord('a') + c)] * half[c])

            left_part = ''.join(candidate)

            if n % 2:
                palindrome = left_part + mid + left_part[::-1]
            else:
                palindrome = left_part + left_part[::-1]

            return palindrome > target

        for _ in range(half_len):
            found = False

            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                left.append(chr(ord('a') + c))

                if feasible():
                    found = True
                    break

                left.pop()
                half[c] += 1

            if not found:
                return ""

        left = ''.join(left)

        if n % 2:
            ans = left + mid + left[::-1]
        else:
            ans = left + left[::-1]

        return ans if ans > target else ""