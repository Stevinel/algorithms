OPERATIONS = {
    '+': lambda a, b: b + a,
    '-': lambda a, b: b - a,
    '*': lambda a, b: b * a,
    '/': lambda a, b: b // a
    }


class Calculator:
    def __init__(self):
        self.__item = []

    def push(self, value):
        self.__item.append(value)

    def pop(self):
        if not self.__item:
            raise IndexError("empty stack")
        return self.__item.pop()
    
    
def parsing_values(input_data):
    for value in input_data:
        if value not in OPERATIONS:
            calc.push(int(value))
        else:
            a, b = calc.pop(), calc.pop()
            calc.push(OPERATIONS[value](a, b))
    return calc.pop()

if __name__ == '__main__':
    calc = Calculator()
    print(parsing_values(input().split()))
