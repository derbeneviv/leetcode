from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        add = False
        for ind, i in enumerate(digits):
            add = False
            digits[ind] = i + 1
            if digits[ind] > 9:
                add = True
                digits[ind] = digits[ind] % 10
            else:
                break
        if add:
            digits.append(1)
        digits.reverse()
        return digits

sol = Solution()
digits = [9, 9, 9]
print(sol.plusOne(digits))