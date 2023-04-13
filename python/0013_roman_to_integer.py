class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman_map = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000}
        for ind, i in enumerate(s):
            if ind > 0 and roman_map[i] > roman_map[s[ind-1]]:
                res = res + roman_map[i] - roman_map[s[ind-1]] - roman_map[s[ind-1]]
            else:
                res = res + roman_map[i]
        return res


sol = Solution()
print(sol.romanToInt("IIIII"))
