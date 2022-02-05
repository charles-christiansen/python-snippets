## [-1,2,6,8,10,14,28,92,104,430] target=6
## len=10, idx=5, nums[idx]=10, pidx=5, idx=2, nums[idx]=2, idx=3, nums[idx]=6,
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
