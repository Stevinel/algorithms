from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """Runtime: 320ms"""
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()

        while headA: 
            node_set.add(headA)
            headA = headA.next
            
        while headB:
            if headB in node_set: 
                return headB
            headB = headB.next
