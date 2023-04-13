# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printAll(self):
        print(f'{self.val}')
        if self.next:
            self.next.printAll()
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.val == val:
            head.next = self.removeElements(head.next, val)
            return head.next
        else:
            head.next = self.removeElements(head.next, val)
            return head



list_node4 = ListNode(2)
list_node3 = ListNode(4, next = list_node4)
list_node2 = ListNode(2, next=list_node3)
list_node1 = ListNode(1, next=list_node2)
val = 2

sol = Solution()

res = sol.removeElements(None, val)
#res.printAll()