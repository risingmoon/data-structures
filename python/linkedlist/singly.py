class SinglyNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '%s' % str(self.value)

    def __repr__(self):
        return '<SinglyNode:%s>' % str(self)


class SinglyLinkedList:

    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def __len__(self):
        return sum(1 for i in self)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return ', '.join(str(n) for n in self)

    def __getitem__(self, node):
        for n in self:
            if n is node:
                return n
        raise LookupError("Node cannot be found")

    def __delitem__(self, node):
        for n in self:
            if n.next is node:
                n.next = n.next.next
                break
        else:
            raise KeyError("Node cannot be found")

    def __reversed__(self):
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
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next, self.head = self.head, node

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next, self.tail = node, node
