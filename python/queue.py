from linkedlist import LinkedList


class Queue(LinkedList):

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        node = self.head
        self.head = self.head.next
        return node
