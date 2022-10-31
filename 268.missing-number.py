from typing import List
#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i, v in enumerate(nums):
            s ^= v
            s ^= i
        s ^= len(nums)
        return s
# @lc code=end

