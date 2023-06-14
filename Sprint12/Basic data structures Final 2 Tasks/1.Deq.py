# n - количество команд
# m — максимальный размер дека
# push_back(value) – добавить элемент в конец дека
# push_front(value) – добавить элемент в начало дека
# pop_front() – вывести первый элемент дека и удалить его
# pop_back() – вывести последний элемент дека и удалить его


# ID 88200060
class DoubleEndedQueue:
    def __init__(self, max_deq_size):
        self.queue = [None] * max_deq_size
        self.max_deq_size = max_deq_size
        self.head = 1
        self.tail = 0
        self.size = 0

    # Проверка на пустую очереди
    def is_empty(self):
        return self.size == 0

    # Добавление в конец очереди
    def push_back(self, token):
        if self.size >= self.max_deq_size:
            raise IndexError("Queue is full")
        else:
            self.tail = (self.tail + 1) % self.max_deq_size
            self.queue[self.tail] = token
            self.size += 1

    # Добавление в начала очереди
    def push_front(self, token):
        if self.size >= self.max_deq_size:
            raise IndexError("Queue is full")
        else:
            self.head = (self.head - 1) % self.max_deq_size
            self.queue[self.head] = token
            self.size += 1

    # Извлечение из конца очереди
    def pop_back(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        token = self.queue[self.tail]
        # self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_deq_size
        self.size -= 1
        return token

    # Извлечение из начала очереди
    def pop_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        token = self.queue[self.head]
        # self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_deq_size
        self.size -= 1
        return token


if __name__ == '__main__':
    count_commands = int(input())
    max_size = int(input())
    queue = DoubleEndedQueue(max_size)
    for _ in range(count_commands):
        command = input()
        operation, *value = command.split()
        try:
            result = getattr(queue, operation)(*value)
            if result is not None:
                print(result)
        except AttributeError:
            print('error')
        except IndexError:
            print('error')

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
