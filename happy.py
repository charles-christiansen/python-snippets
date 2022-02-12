## Happy Number Algorithm
## LeetCode: https://leetcode.com/problems/happy-number
## Given an integer, determine if the integer is a happy number.
## A happy number is one where continuously squaring the digits
## and summing the squares eventually results in the sum of the
## squares being 1.
class Solution:
    def isHappy(self, n: int) -> bool:
        digitSets=[]
        curNum=n
        sum=0
        while True:
            digits=[int(digit) for digit in str(curNum)]
            for d in digits:
                sum+=d*d
            if sum==1:
                return True
            else:
                curNum=sum
                # sort the digits in this sum & compare to
                # sets of digits we've already run. If it
                # exists in the list, we're in an endless
                # loop and should return False. If not,
                # put this set of digits into the list
                # and keep going.
                sum=int("".join(sorted([i for i in str(sum)])))
                try:
                    idx=digitSets.index(sum)
                    return False
                except:
                    digitSets.append(sum)
                    sum=0

s=Solution()
# return True
print(s.isHappy(1))
# return False
print(s.isHappy(24))
# return True
print(s.isHappy(19))
