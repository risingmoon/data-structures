class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '<SinglyNode:%s>' % str(self)

    def __str__(self):
        return '%s' % str(self.value)


class LinkedList:

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

    def __getitem__(self, value):
        for n in self:
            if n.value == value:
                return n
        raise LookupError("Node cannot be found")

    @staticmethod
    def search(linkedlist, value):
        return linkedlist[value]
