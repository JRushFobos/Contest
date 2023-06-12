# ID
import operator


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


if __name__ == '__main__':
    stack = Stack()
    elements = input().split()
    for element in elements:
        if element.lstrip('-').isdigit():
            stack.push(int(element))
        else:
            if stack.size() < 2:
                raise IndexError
            else:
                number1 = stack.pop()
                number2 = stack.pop()
                stack.push(OPERATORS[element](number2, number1))

    print(stack.pop())
