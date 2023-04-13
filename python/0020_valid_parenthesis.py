import queue
class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        open_parenthesis = parenthesis.keys()

        q = []
        for i in s:
            if i in open_parenthesis:
                q.append(i)
            if i not in open_parenthesis:
                if len(q) == 0:
                    return False
                j = q.pop()
                if parenthesis[j] != i:
                    return False
        if len(q) != 0:
            return False
        return True


sol = Solution()
print(sol.isValid("]"))