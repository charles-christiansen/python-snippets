import math as math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lower=0
        upper=len(nums)-1
        while(upper >= lower):
            idx=math.floor((upper+lower)/2)
            if(nums[idx]==target):
                return idx
            elif(nums[idx] < target):
                lower=idx+1
            else:
                upper=idx-1
        return -1

s=Solution()
print(s.search([-1,0,3,5,9,12],32))
print(s.search([-1,0,3,5,9,12],2))
