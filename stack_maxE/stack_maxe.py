class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) == 0:
            self.items.append([item, item])
        else:
            if item > self.peek()[1]:
                self.items.append([item, item])
            else:
                self.items.append([item, self.peek()[1]])

    def pop(self):
        if len(self.items) == 0:
            print('error')
            return
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def get_max(self):
        if len(self.items) == 0:
            print('None')
            return
        print(self.peek()[1])


if __name__ == '__main__':
    stack = Stack()
    length = int(input())
    for i in range(0, length):
        command = input()
        if command == 'get_max':
            stack.get_max()
        elif command == 'pop':
            stack.pop()
        else:
            stack.push(int(command.split()[1]))
