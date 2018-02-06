from unittest import TestCase

from linkedlist.singly import SinglyNode, SinglyLinkedList, Stack, Queue
from linkedlist.singly import UnderflowError


class SinglyNodeTestCase(TestCase):
    pass


class SinglyLinkedListTestCase(TestCase):

    def setUp(self):
        self.linkedlist = SinglyLinkedList()
        self.nodes = [SinglyNode(x) for x in range(3)]

        for n in self.nodes:
            self.linkedlist.append(n)

    def test_init_empty_list_head_and_tail_is_null(self):
        linkedlist = SinglyLinkedList()
        self.assertIsNone(linkedlist.head)
        self.assertIsNone(linkedlist.tail)

    def test_init_empty_list_length_is_zero(self):
        linkedlist = SinglyLinkedList()
        self.assertEqual(len(linkedlist), 0)

    def test_getitem_valid_list_get_existing_node_is_found(self):
        node_int = self.nodes[1]

        self.assertIs(self.linkedlist[node_int.value], node_int)

    def test_getitem_valid_list_get_nonexistent_node_raises_lookuperror(self):
        node = SinglyNode(None)

        self.assertRaises(LookupError, self.linkedlist.__getitem__, node.value)

    def test_delitem_valid_list_delete_node_removes_node(self):
        node_int = self.nodes[1]
        nodes = [self.nodes[0], self.nodes[2]]

        del self.linkedlist[node_int]

        for key, value in zip(self.linkedlist, nodes):
            self.assertIs(key, value)

    def test_delitem_valid_list_delete_head_replaces_head(self):
        del self.linkedlist[self.nodes[0]]

        self.assertIs(self.linkedlist.head, self.nodes[1])
        self.assertEqual(len(self.linkedlist), 2)

    def test_delitem_valid_list_delete_all_empties_list(self):
        for n in self.nodes:
            del self.linkedlist[n]

        self.assertIsNone(self.linkedlist.head)
        self.assertIsNone(self.linkedlist.tail)
        self.assertEqual(len(self.linkedlist), 0)

    def test_delitem_valid_list_delete_tail_replaces_tail(self):
        del self.linkedlist[self.nodes[2]]

        self.assertIs(self.linkedlist.tail, self.nodes[1])
        self.assertEqual(len(self.linkedlist), 2)

    def test_delitem_valid_list_delete_non_existent_node_raises_lookuperror(self): # noqa E501
        node = SinglyNode('nonexistent')

        self.assertRaises(LookupError, self.linkedlist.__delitem__, node)

    def test_reversed_valid_list_reverses_nodes(self):
        reversed(self.linkedlist)

        for key, value in zip(self.linkedlist, reversed(self.nodes)):
            self.assertIs(key, value)

    def test_prepend_empty_list_prepend_node_is_head_and_tail(self):
        node_string = SinglyNode('head')
        linkedlist = SinglyLinkedList()

        linkedlist.prepend(node_string)

        self.assertIs(linkedlist.head, node_string)
        self.assertIs(linkedlist.tail, node_string)
        self.assertIsNone(linkedlist.head.next)
        self.assertEqual(len(linkedlist), 1)

    def test_prepend_valid_list_prepend_node_is_head(self):
        node_string = SinglyNode('head')

        self.linkedlist.prepend(node_string)

        self.assertIs(self.linkedlist.head, node_string)
        self.assertEqual(node_string.next, self.nodes[0])
        self.assertEqual(len(self.linkedlist), 4)

    def test_append_empty_list_append_node_is_head_and_tail(self):
        node = SinglyNode('head')
        linkedlist = SinglyLinkedList()

        linkedlist.append(node)

        self.assertIs(linkedlist.head, node)
        self.assertIs(linkedlist.tail, node)
        self.assertEqual(len(linkedlist), 1)

    def test_append_empty_list_append_node_is_tail(self):
        node = SinglyNode('head')
        linkedlist = SinglyLinkedList()

        linkedlist.append(node)

        self.assertIs(linkedlist.tail, node)
        self.assertEqual(len(linkedlist), 1)

    def test_append_valid_list_append_node_is_tail(self):
        node = SinglyNode('tail')
        self.linkedlist.append(node)

        self.assertIs(self.linkedlist.tail, node)
        self.assertEqual(len(self.linkedlist), 4)

    def test_search_empty_list_raise_keyerror(self):
        linkedlist = SinglyLinkedList()
        with self.assertRaises(LookupError):
            SinglyLinkedList.search(linkedlist, 'nonexistent')

    def test_search_valid_list_with_nonexistent_key_raise_lookuperror(self):
        with self.assertRaises(LookupError):
            SinglyLinkedList.search(self.linkedlist, 'nonexistent')

    def test_search_valid_list_with_existent_key_return_node(self):
        node = SinglyLinkedList.search(self.linkedlist, self.nodes[2].value)
        self.assertIs(node, self.nodes[2])

    def test_insert_empty_list_head_and_tail_is_same_node(self):
        node = SinglyNode('head')
        linkedlist = SinglyLinkedList()
        SinglyLinkedList.insert(linkedlist, node)

        self.assertIs(linkedlist.head, node)
        self.assertIs(linkedlist.tail, node)
        self.assertIsNone(node.next)
        self.assertEqual(len(linkedlist), 1)

    def test_insert_valid_list_head_is_new_node(self):
        node = SinglyNode('head')
        SinglyLinkedList.insert(self.linkedlist, node)

        self.assertIs(self.linkedlist.head, node)
        self.assertEqual(len(self.linkedlist), 4)

    def test_delete_empty_list_raises_lookuperror(self):
        linkedlist = SinglyLinkedList()

        with self.assertRaises(LookupError):
            del linkedlist[self.nodes[0]]

    def test_delete_valid_list_nonexistent_node_lookuperror(self):
        with self.assertRaises(LookupError):
            del self.linkedlist[SinglyNode('nonexistent')]

    def test_delete_valid_list_existent_key_delete_node(self):
        del self.linkedlist[self.nodes[2]]
        self.assertIs(self.linkedlist.tail, self.nodes[1])

        del self.linkedlist[self.nodes[0]]
        self.assertIs(self.linkedlist.head, self.nodes[1])


class StackTestCase(TestCase):

    def setUp(self):
        self.nodes = [SinglyNode(x) for x in range(10)]
        self.stack = Stack()
        for n in self.nodes:
            self.stack.push(n)

    def test_init_empty_stack_top_is_none(self):
        stack = Stack()

        self.assertIsNone(stack.top)
        self.assertEqual(len(stack), 0)

    def test_push_empty_stack_top_is_node(self):
        node = SinglyNode(0)
        stack = Stack()

        stack.push(node)

        self.assertIs(stack.top, node)
        self.assertEqual(len(stack), 1)

    def test_push_valid_stack_adds_node(self):
        node = SinglyNode(10)
        self.stack.push(node)

        nodes = self.nodes + [node]

        for n, s in zip(reversed(nodes), self.stack):
            self.assertIs(n, s)
        self.assertEqual(len(self.stack), 11)

    def test_pop_empty_stack_raises_underflowerror(self):
        stack = Stack()

        with self.assertRaises(UnderflowError):
            stack.pop()

    def test_pop_valid_stack_removes_node(self):
        node = self.stack.pop()

        self.assertIs(node, self.nodes[9])
        for n, s in zip(self.stack, reversed(self.nodes[:9])):
            self.assertIs(n, s)

        self.assertEqual(len(self.stack), 9)

    def test_pop_valid_stack_removes_all_top_is_none(self):
        for i in range(10):
            self.stack.pop()

        self.assertIsNone(self.stack.top)
        self.assertEqual(len(self.stack), 0)


class QueueTestCase(TestCase):

    def setUp(self):
        self.nodes = [SinglyNode(x) for x in range(10)]
        self.queue = Queue()
        for n in self.nodes:
            self.queue.enqueue(n)

    def test_init_empty_queue_head_and_tail_is_none(self):
        queue = Queue()

        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        self.assertEqual(len(queue), 0)

    def test_enqueue_empty_queue__head_and_tail_same_node(self):
        node = SinglyNode(0)
        queue = Queue()
        queue.enqueue(node)

        self.assertIs(queue.head, node)
        self.assertIs(queue.tail, node)
        self.assertEqual(len(queue), 1)

    def test_enqueue_valid_queue_enqueue_adds_node_to_tail(self):
        node = SinglyNode(10)
        self.queue.enqueue(node)

        self.assertIs(self.queue.tail, node)
        self.assertIs(self.queue.head, self.nodes[0])

    def test_dequeue_empty_queue_raises_underflowerror(self):
        queue = Queue()

        with self.assertRaises(UnderflowError):
            queue.dequeue()

    def test_dequeue_valid_queue_removes_node(self):
        node = self.queue.dequeue()

        self.assertIs(node, self.nodes[0])
        self.assertIs(self.queue.tail, self.nodes[9])
        self.assertEqual(len(self.queue), 9)

    def test_dequeue_valid_queue_removes_all_head_and_tail_is_none(self):
        for i in range(10):
            self.queue.dequeue()

        self.assertIsNone(self.queue.head)
        self.assertIsNone(self.queue.tail)
        self.assertEqual(len(self.queue), 0)
