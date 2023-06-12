# n - количество команд
# m — максимальный размер дека
# push_back(value) – добавить элемент в конец дека
# push_front(value) – добавить элемент в начало дека
# pop_front() – вывести первый элемент дека и удалить его
# pop_back() – вывести последний элемент дека и удалить его


class DoubleEndedQueue:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_n = m
        self.head = 0
        self.tail = 0
        self.size = 0

    # Проверка на пустую очереди
    def is_empty(self):
        return self.size == 0

    # Добавление в конец очереди
    def push_back(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    # Добавление в начала очереди
    def push_front(self, x):
        if self.size < self.max_n:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    # Извлечение из конца очереди
    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.tail - 1]
        # self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

    # Извлечение из начала очереди
    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.head]
        # self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    # def print_queue(self):
    #     return self.queue


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

        # if value:
        #     try:
        #         result = commands[operation](int(value[0]))
        #     except:
        #         print('error')
        # else:
        #     result = commands[operation]()
        # if result is not None:
        #     print(result)
# Тест №1
# queue = DoubleEndedQueue(4)
# queue.push_front(861)
# queue.push_front(-819)
# print('GO')
# print(queue.print_queue())
# print(queue.pop_back())
# print(queue.pop_back())

# Тест №2
# queue = DoubleEndedQueue(6)
# queue.push_front(-855)
# queue.push_front(0)
# print(queue.print_queue())
# print(queue.pop_back())
# print(queue.pop_back())
# queue.push_back(844)
# print(queue.pop_back())
# queue.push_back(823)
# print('Result')
# print(queue.print_queue())

# Тест №3
# queue = DoubleEndedQueue(6)
# queue.push_front(-201)
# queue.push_back(959)
# queue.push_back(102)
# queue.push_front(20)
# print(queue.pop_front())
# print(queue.pop_back())