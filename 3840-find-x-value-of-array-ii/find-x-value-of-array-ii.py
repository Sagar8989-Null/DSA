from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int,
                    queries: List[List[int]]) -> List[int]:

        n = len(nums)

        size = 4 * n

        prod = [1] * size
        cnt = [[0] * k for _ in range(size)]

        def merge(node, left, right):
            prod[node] = (prod[left] * prod[right]) % k

            for r in range(k):
                cnt[node][r] = cnt[left][r]

            for r in range(k):
                new_r = (prod[left] * r) % k
                cnt[node][new_r] += cnt[right][r]

        def build(node, l, r):
            if l == r:
                p = nums[l] % k
                prod[node] = p
                cnt[node][p] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, node * 2, node * 2 + 1)

        def update(node, l, r, idx, value):
            if l == r:
                p = value % k

                prod[node] = p

                for x in range(k):
                    cnt[node][x] = 0

                cnt[node][p] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            merge(node, node * 2, node * 2 + 1)

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return 1 % k, [0] * k

            if ql <= l and r <= qr:
                return prod[node], cnt[node][:]

            mid = (l + r) // 2

            left_prod, left_cnt = query(
                node * 2, l, mid, ql, qr
            )

            right_prod, right_cnt = query(
                node * 2 + 1, mid + 1, r, ql, qr
            )

            result_prod = (left_prod * right_prod) % k
            result_cnt = left_cnt[:]

            for x in range(k):
                new_x = (left_prod * x) % k
                result_cnt[new_x] += right_cnt[x]

            return result_prod, result_cnt

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            update(1, 0, n - 1, index, value)

            _, counts = query(1, 0, n - 1, start, n - 1)

            ans.append(counts[x])

        return ans