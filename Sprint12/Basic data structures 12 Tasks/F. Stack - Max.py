#  Стек - Макс


class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return "error"

        popped_element = self.stack.pop()

        if popped_element == self.max_stack[-1]:
            self.max_stack.pop()

    def get_max(self):
        if not self.max_stack:
            return "None"

        return self.max_stack[-1]


n = int(input())

stack = StackMax()

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        x = int(command[1])
        stack.push(x)
    elif command[0] == "pop":
        result = stack.pop()
        if result == "error":
            print("error")
    elif command[0] == "get_max":
        max_value = stack.get_max()
        print(max_value)
