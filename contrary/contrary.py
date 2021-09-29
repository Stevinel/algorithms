class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def print_list(head):
    while head:
        print(head.value, end='\n' if head.next else '')
        head = head.next

def solution(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail
