from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def recursive_search(nums: List[int], target: int, start: int) -> int:
            length = len(nums)
            half = length // 2
            if nums:
                if nums[half] > target:
                    return recursive_search(nums[:half], target, start)
                elif nums[half] < target:
                    return recursive_search(nums[half+1:], target, start+half+1)
            return start+half
        return recursive_search(nums, target, 0)




sol = Solution()
nums = []
target = 7
print(sol.searchInsert(nums, target))
