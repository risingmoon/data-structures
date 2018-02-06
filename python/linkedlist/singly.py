from linkedlist import Node, LinkedList


class UnderflowError(ArithmeticError):
    pass


class SinglyNode(Node):
    pass


class SinglyLinkedList(LinkedList):

    @staticmethod
    def insert(linkedlist, node):
        linkedlist.prepend(node)

    @staticmethod
    def delete(linkedlist, node):
        del linkedlist[node]

    def __delitem__(self, node):
        for n in self:
            if node is self.head:
                if self.head.next is None:
                    self.tail = None
                self.head = self.head.next
                break
            if n.next is node:
                n.next = n.next.next
                if n.next is not None:
                    n.next.next = None
                else:
                    self.tail = n
                break
        else:
            raise LookupError("Node cannot be found")

    def __reversed__(self):
        """Reverse singly linkedlist non-recursively"""
        node = self.head
        next_node = node.next
        while next_node:
            next_next_node = next_node.next
            next_node.next = node
            node = next_node
            next_node = next_next_node

        self.head, self.tail = self.tail, self.head
        self.tail.next = None

    def prepend(self, node):
        """Insert to head with O(1) complexity"""
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append(self, node):
        """Insert to tail with O(1) complexity"""
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


class Stack(LinkedList):
    """
    Exercise 10.2-2

    Implement a stack with singly linked list
    """

    def push(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is not None:
            node = self.head
            self.head = self.head.next
            return node
        raise UnderflowError("Stack Underflow")


class Queue(LinkedList):
    """
    Exercise 10.2-3

    Implement a queue with singly linked list
    """

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
