class Deque:
    def __init__(self, n):
        self.__item = [None] * n
        self.__max_length = n
        self.__front = 0
        self.__back = 1
        self.__size = 0

    def push_front(self, value):
        if self.__size == self.__max_length:
            raise IndexError("overflow error")
        self.__item[self.__front] = value
        self.__front = (self.__front - 1) % self.__max_length
        self.__size += 1

    def push_back(self, value):
        if self.__size == self.__max_length:
            raise IndexError("overflow error")
        self.__item[self.__back] = value
        self.__back = (self.__back + 1) % self.__max_length
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise IndexError("empty error")
        shift_right_side = (self.__front + 1) % self.__max_length
        value = self.__item[shift_right_side]
        self.__front = shift_right_side
        self.__item[self.__front] = None
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__size == 0:
            raise IndexError("empty error")
        shift_left_side = (self.__back - 1) % self.__max_length
        value = self.__item[shift_left_side]
        self.__back = shift_left_side
        self.__item[self.__back] = None
        self.__size -= 1
        return value


if __name__ == "__main__":
    count_commands = int(input())
    deque = Deque(int(input()))
    COMMAND_DICT = {
        "push_front": lambda value: deque.push_front(value),
        "push_back": lambda value: deque.push_back(value),
        "pop_front": lambda: deque.pop_front(),
        "pop_back": lambda: deque.pop_back(),
    }
    commands = []
    for elements in range(count_commands):
        commands.append(input())
    for command in commands:
        instruction, *value = command.split()
        try:
            result = COMMAND_DICT[instruction](*value)
            if result is not None:
                print(result)
        except IndexError:
            print("error")
        except KeyError:
            print("Unknown method")
