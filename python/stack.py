from linkedlist import LinkedList


class UnderflowError(ArithmeticError):
    pass


class Stack(LinkedList):

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
