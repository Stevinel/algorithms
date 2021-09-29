class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        try:
            print(max(self.items))
        except ValueError:
            print('None')


if __name__ == '__main__':
    stack = StackMax()
    count = int(input())
    for elem in range(count):
        elem = input()
        if elem == 'get_max':
            stack.get_max()
        elif elem == 'pop':
            stack.pop()
        else:
            stack.push(int(elem.split()[1]))
