from linkedlist import Node, LinkedList


class SinglyNode(Node):
    pass


class SinglyLinkedList(LinkedList):

    def __delitem__(self, node):
        for n in self:
            if n.next is node:
                n.next = n.next.next
                n.next.next = None
                break
        else:
            raise KeyError("Node cannot be found")

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
