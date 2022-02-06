## Longest Substring Without Repeating Characters
## LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
## Given a String, find the longest sustring of the string
## which contains no repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ns=""
        longest=0
        for c in s:
            try:
                idx=ns.index(c)
                if len(ns) > longest:
                    longest=len(ns)
                ns=ns[idx+1:len(ns):1]+c
            except:
                ns+=c
        if len(ns) > longest:
            return len(ns)
        else:
            return longest

s=Solution()
# return 7
print(s.lengthOfLongestSubstring("alphabet"))
# return 15
print(s.lengthOfLongestSubstring("abcdefghijklmamamamamnopqrstuvwxyz"))
# return 3
print(s.lengthOfLongestSubstring("abcabcbb"))
# return 1
print(s.lengthOfLongestSubstring("bbbbb"))
# return 3
print(s.lengthOfLongestSubstring("pwwkew"))
