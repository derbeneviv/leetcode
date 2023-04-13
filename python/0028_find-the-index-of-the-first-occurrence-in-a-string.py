class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for ind, i in enumerate(haystack):
            res = ind
            k = 0
            for j in needle:
                try:
                    if haystack[ind+k] == j:
                        k = k+1
                        continue
                    else:
                        res = -1
                        break
                except IndexError:
                    return -1
            if res >= 0:
                return res
        return res


sol = Solution()
haystack = "saadbutssdad"
needle = "sad"
print(sol.strStr(haystack, needle))
