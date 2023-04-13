# Definition for singly-linked list.
from typing import Optional
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printAll(self):
        print(f'{self.val}')
        if self.next:
            self.next.printAll()

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = list1
        pointer = list1
        while pointer:
            if list2.val <= list1.next.val:
                list1_temp = list1.next
                list2_temp = list2.next
                list1.next = list2
                list2.next = list1_temp
                list2 = list2_temp
            list1 = list1.next
            pointer = list1.next
            result.printAll()
            print('-----------')
        return result

sol = Solution()
list1_node3 = ListNode(4)
list1_node2 = ListNode(2, next=list1_node3)
list1_node1 = ListNode(1, next=list1_node2)
list1_node1.printAll()
print('-----------')
list2_node3 = ListNode(4)
list2_node2 = ListNode(3, next=list2_node3)
list2_node1 = ListNode(1, next=list2_node2)
list2_node1.printAll()
print('++++++++++++++')


print(sol.mergeTwoLists(list1_node1, list2_node1).printAll())
