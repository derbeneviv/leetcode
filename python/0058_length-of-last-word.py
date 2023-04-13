class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        arr = s.split(' ')
        arr.reverse()
        for i in arr:
            if len(i) > 0:
                return len(i)
        return res

sol = Solution()
s = "Today is a nice day"
print(sol.lengthOfLastWord(s))