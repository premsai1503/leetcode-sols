from typing import List
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = [0] * 32
        for num in nums:
            b = f'{num:032b}'
            for i, v in enumerate(b):
                if v == '1':
                    cnt[i] += 1
        s = ''
        for i in cnt:
            if i > len(nums) / 2:
                s += '1'
            else:
                s += '0'
        return int(s, base=2)
# @lc code=end

