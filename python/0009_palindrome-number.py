class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        mylist = []
        while x > 0:
            mod = x%10
            mylist.append(mod)
            x = x//10
        newx = 0
        for ind, i in enumerate(mylist):
            if ind > half_size:
                break
            if mylist[ind] == mylist[-ind-1]:
                continue
            else:
                return False
        return True

sol = Solution()
print(sol.isPalindrome(1233321))
