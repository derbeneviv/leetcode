class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta = 0
        intb = 0
        for ind, i in enumerate(a[::-1]):
            to_add = 0
            if a[::-1][ind] == '1':
                to_add = 1
            inta = inta + (to_add*pow(2, ind))

        for ind, i in enumerate(b[::-1]):
            to_add = 0
            if b[::-1][ind] == '1':
                to_add = 1
            intb = intb + (to_add * pow(2, ind))
        return str(bin(inta + intb)).replace('0b','')

sol = Solution()
a = "1010"
b = "1011"
print(sol.addBinary(a, b))