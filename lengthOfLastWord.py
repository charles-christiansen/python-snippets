## Length of Last Word
## LeetCode: https://leetcode.com/problems/length-of-last-word/
## Given a string s consisting of some words separated by some
## number of spaces, return the length of the last word in the string.
## s is guaranteed to contain at least one word.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==1:
            return 1

        strlen=0
        revs=list(reversed(s))
        for char in revs:
            if char!=" ":
                strlen += 1
            elif strlen > 0:
                return strlen
        return strlen
s=Solution()
# Print 1
print(s.lengthOfLastWord("x"))
# Also print 1
print(s.lengthOfLastWord("             x             "))
# Print 7
print(s.lengthOfLastWord("This is an outrage"))
# Also print 7
print(s.lengthOfLastWord("This           is an           outrage     "))
# Print 1
print(s.lengthOfLastWord("a "))
