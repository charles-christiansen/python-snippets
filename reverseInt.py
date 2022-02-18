## Remove Value from List
## LeetCode: https://leetcode.com/problems/reverse-integer/
## Given a signed 32-bit integer, reverse the digits and return
## the resulting integer. If the result is out of bounds of
## a 32-bit integer, return 0.
class Solution:
    def reverse(self, x: int) -> int:
        digits=list(reversed([digit for digit in str(x)]))
        if digits[len(digits)-1]=="-":
            digits.remove("-")
            digits.insert(0,"-")
        revx=int("".join(digits))
        if revx < -2**31 or revx > 2**31 - 1:
            return 0
        return revx

s=Solution()
x=-2**20
print(s.reverse(456))
print(s.reverse(-1290))
print(s.reverse(x))
