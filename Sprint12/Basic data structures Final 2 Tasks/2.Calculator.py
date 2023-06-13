# ID 88166944
import operator


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, item):
        self.__elements.append(item)

    def pop(self):
        if len(self.__elements) == 0:
            raise IndexError("Stack is empty")
        return self.__elements.pop()


def main(stack, elements, convertor=int):
    for element in elements:
        if element in OPERATORS:
            right, left = stack.pop(), stack.pop()
            stack.push(OPERATORS[element](left, right))
        else:
            stack.push(convertor(element))

    print(stack.pop())


if __name__ == '__main__':
    stack = Stack()
    elements = input().split()
    main(stack, elements)
