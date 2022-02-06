## Implement strStr()
## LeetCode: https://leetcode.com/problems/implement-strstr
## Given a haystack and a needle, find the needle
## in the haystack and return the index. If the needle is
## an empty string, return 0. If the needle is not found
## return -1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1

s=Solution()
# return 2
print(s.strStr("hello","ll"))
# return -1
print(s.strStr("aaaaa","bba"))
# return 0
print(s.strStr("",""))
# return 0
print(s.strStr("lucky",""))
# return -1
print(s.strStr("","unl"))
