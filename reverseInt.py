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
