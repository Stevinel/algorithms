from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        
        while(head):
            if head.val not in values:
                values.append(head.val)
            head = head.next

        first_node = ListNode()
        last_node = first_node

        for i in values:
            last_node.next = ListNode(i)
            last_node = last_node.next
        return first_node.next
