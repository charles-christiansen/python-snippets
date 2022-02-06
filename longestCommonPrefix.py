## Longest Common Prefix
## LeetCode: https://leetcode.com/problems/longest-common-prefix/
## Given a list of words, find the longest common prefix
## of all words in the list. Return empty string if there is
## no common prefix.
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        n=len(strs)-1
        flat=",".join(strs)
        shortest=strs[0]
        idxEnd=len(shortest)
        while idxEnd >= 0:
            substring=shortest[0:idxEnd:1]
            testString=","+substring
            count=flat.count(testString)
            if count == n:
                return substring
            idxEnd -= 1
        return ""

s=Solution()
# Return fl
print(s.longestCommonPrefix(["flower","flow","flight"]))
# Return empty string
print(s.longestCommonPrefix(["dog","racecar","car"]))
# Return flo
print(s.longestCommonPrefix(["flower","flowbee","flowchart","floodlamp"]))
