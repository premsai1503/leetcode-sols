#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # b = f'{n:032b}'
        # return sum([1 if c == '1' else 0 for c in b])
        cnt = 0
        while n != 0:
            n = n & (n - 1)
            cnt += 1
        return cnt
# @lc code=end

