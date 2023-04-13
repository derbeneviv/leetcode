from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        try:
            start = nums.index(val)
        except ValueError:
            return len(nums)
        nums.reverse()
        end = nums.index(val)
        nums.reverse()
        end = len(nums)-end
        for i in range(0, end-start, 1):
            nums.pop(start)
        return len(nums)


sol = Solution()
nums = []
val = 2
print(sol.removeElement(nums, val))
print(nums)
