from collections import deque
from typing import List
#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        m = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        cnt = set()
        res = set()
        si = 0
        ss = deque()
        for i in range(10):
            si = si << 2
            si += m[s[i]]
            ss.append(s[i])
        cnt.add(si)
        for i in range(len(s) - 10):
            si = si << 2
            si += m[s[i + 10]]
            si -= (m[s[i]] << 20)
            ss.popleft()
            ss.append(s[i + 10])
            if si in cnt:
                res.add(''.join(ss))
            cnt.add(si)
        return res
# @lc code=end

