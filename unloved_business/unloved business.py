class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value

def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, idx):
    if idx == 0:
        return node.next_item
    previous_node = get_node_by_index(node, idx-1)
    next_node = get_node_by_index(node, idx+1)
    previous_node.next_item = next_node
    return node

