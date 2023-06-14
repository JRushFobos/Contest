# ID 88202472
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
        try:
            return self.__elements.pop()
        except IndexError:
            raise IndexError("Stack is empty")


def main(elements, convertor=int, operators=OPERATORS):
    stack = Stack()
    for element in elements:
        if element in operators:
            right, left = stack.pop(), stack.pop()
            stack.push(operators[element](left, right))
        else:
            try:
                stack.push(convertor(element))
            except TypeError:
                print('Incorrect type element')

    return stack.pop()


if __name__ == '__main__':
    elements = input().split()
    print(main(elements))
