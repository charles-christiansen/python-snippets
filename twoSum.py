class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            n1=nums[i]
            n2=target-n1
            try:
                j=nums.index(n2,i+1)
                return[i,j]
            except:
                continue

s=Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,2,4],6))
print(s.twoSum([3,3],6))
print(s.twoSum([1,3,5,7,9,11,13,15,18,19],25))
