class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value

def lenght(node):
    count = 0
    while node is not None:
        count += 1
        node = node.next_item
    return count


def index(node, count):
    idx = count
    while node:
        idx -= 1
        node = node.next_item
    return idx


def solution(node, elem):
    count = lenght(node)
    while node:
        if elem == node.value:
            return index(node, count)
        else:
            node = node.next_item
    return -1
