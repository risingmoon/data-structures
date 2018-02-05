from linkedlist import Node, LinkedList


class SinglyNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.next = None

    def __str__(self):
        return '%s' % str(self.value)


class SinglyLinkedList(LinkedList):

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
