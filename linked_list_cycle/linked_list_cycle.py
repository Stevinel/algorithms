from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """Runtime: 110ms"""
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False


# class Solution:
#     """Runtime: 3219ms"""
#     def has_cycle(self, head: Optional[ListNode]) -> bool:
#         val = []
#         while head:
#             try:
#                 if head.next in val:
#                     return True
#                 val.append(head)
#                 head = head.next
#             except Exception as e:
#                 return False