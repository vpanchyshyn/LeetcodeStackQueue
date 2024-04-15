class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        if self.queue1.is_empty():
            self.queue1.add(x)
            while not self.queue2.is_empty():
                self.queue1.add(self.queue2.pop().item)
        else:
            self.queue2.add(x)
            while not self.queue1.is_empty():
                self.queue2.add(self.queue1.pop().item)

    def pop(self) -> int:
        if not self.queue1.is_empty():
            return self.queue1.pop().item
        if not self.queue2.is_empty():
            return self.queue2.pop().item

    def top(self) -> int:
        if not self.queue1.is_empty():
            return self.queue1.peek
        if not self.queue2.is_empty():
            return self.queue2.peek

    def empty(self) -> bool:
        return self.queue1.is_empty() and self.queue2.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
