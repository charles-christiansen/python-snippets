## Guess the number.
## LeetCode: https://leetcode.com/problems/guess-number-higher-or-lower
## Given an integer n, guess a randomly generated number between 1 and n.
## The problem provides a guess function which returns -1, 0, or 1 if the
## provided number is higher, equal to, or lower than the random pick.
import random
import math
class Solution:
    pick=0
    def initPick(self, n: int):
        if n==1:
            self.pick=1
        else:
            self.pick=random.randrange(1,n)
        print("==============================")
        print("The pick is " + str(self.pick))
        print("==============================")

    def guess(self, num: int) -> int:
        if num < self.pick:
            return 1
        if num > self.pick:
            return -1
        return 0

    def guessNumber(self, n: int) -> int:
        if self.pick==0:
            self.initPick(n)
        lower=1
        upper=n
        curGuess=math.floor((upper+lower)/2)
        hilo=self.guess(curGuess)
        while hilo != 0:
            if hilo==1:
                lower=curGuess+1
            else:
                upper=curGuess-1

            curGuess=math.floor((upper+lower)/2)
            hilo=self.guess(curGuess)

        return curGuess

s=Solution()
print(s.guessNumber(129192))
s.pick=0
print(s.guessNumber(1000000))
