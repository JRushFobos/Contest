# ID 88136883
class DoubleEndedQueue:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_n = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, x):
        if self.size < self.max_n:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.tail - 1]
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


if __name__ == '__main__':
    count_commands = int(input())
    max_size = int(input())
    queue = DoubleEndedQueue(max_size)
    commands = {
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
        'push_back': queue.push_back,
        'push_front': queue.push_front,
    }
    for i in range(count_commands):
        command = input()
        operation, *value = command.split()
        try:
            result = commands[operation](*map(int, value))
            if result is not None:
                print(result)
        except:
            print('error')
