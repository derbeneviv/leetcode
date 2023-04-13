from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        for ind, i in enumerate(nums):
            if ind == 0:
                continue
            if nums[ind] == nums[ind-1]:
                nums[ind-1] = 101
                k = k-1
        nums.sort()
        return k





sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
print(nums)