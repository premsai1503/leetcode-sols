#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = f'{left:032b}'
        r = f'{right:032b}'
        cnt = 0
        s = ""
        for i in range(32):
            if l[i] == r[i]:
                cnt += 1
                s += l[i]
            else:
                break
        s += ("0" * (32 - cnt))
        return int(s, 2)
# @lc code=end

