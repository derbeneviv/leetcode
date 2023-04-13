from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for ind, word in enumerate(strs):
            reslen = len(result)
            for i in range(0, reslen+1, 1):
                result = result[:reslen - i]
                if word.startswith(result[:reslen-i]):
                    break
        return result


sol = Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))