from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Runtime: 71ms"""
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""

        while(l1):
            str1 += str(l1.val)
            l1 = l1.next
        while(l2):
            str2 += str(l2.val)
            l2 = l2.next 

        result_number =  list(map(int, str(int(str1[::-1]) + int(str2[::-1]))[::-1]))
        first_node = ListNode()
        last_node = first_node

        for i in result_number:
            last_node.next = ListNode(i)
            last_node = last_node.next
        return first_node.next
