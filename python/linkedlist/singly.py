class SinglyNode:

    def __init__(self, value):
        self.value = value
        self._next = None

    def __str__(self):
        return '%s' % str(self.value)

    def __repr__(self):
        return '<SinglyNode:%s>' % str(self)


class SinglyLinkedList:

    def __init__(self, node=None):
        self.head = node

    def __len__(self):
        return sum(1 for i in self)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node._next

    def __str__(self):
        return ', '.join(str(n) for n in self)

    def prepend(self, node):
        if self.head is None:
            self.head = node
        else:
            node._next, self.head = self.head, node

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            for n in self:
                pass
            else:
                n._next = node
