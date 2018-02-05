from unittest import TestCase

from linkedlist.singly import SinglyNode, SinglyLinkedList


class SinglyNodeTestCase(TestCase):
    pass


class SinglyLinkedListTestCase(TestCase):

    def setUp(self):
        self.linkedlist = SinglyLinkedList()
        self.nodes = [
            SinglyNode("node"),
            SinglyNode(20),
            SinglyNode(list(range(6)))]

        for n in self.nodes:
            self.linkedlist.append(n)

    def test_init_empty_list_head_null(self):
        linkedlist = SinglyLinkedList()
        self.assertIsNone(linkedlist.head)

    def test_init_empty_list_length_is_zero(self):
        linkedlist = SinglyLinkedList()
        self.assertEqual(len(linkedlist), 0)

    def test_getitem_valid_list_get_existing_node_is_found(self):
        node_int = self.nodes[1]

        self.assertIs(self.linkedlist[node_int], node_int)

    def test_getitem_valid_list_get_nonexistent_node_raises_exception(self):
        node = SinglyNode(None)

        self.assertRaises(LookupError, self.linkedlist.__getitem__, node)

    def test_delitem_valid_list_delete_node_removes_node(self):
        node_int = self.nodes[1]
        nodes = [self.nodes[0], self.nodes[2]]

        del self.linkedlist[node_int]

        for key, value in zip(self.linkedlist, nodes):
            self.assertIs(key, value)

    def test_delitem_valid_list_delete_non_existent_node_raises_keyerror(self):
        node = SinglyNode('nonexistent')

        self.assertRaises(KeyError, self.linkedlist.__delitem__, node)

    def test_reversed_valid_list_reverses_nodes(self):
        reversed(self.linkedlist)

        for key, value in zip(self.linkedlist, reversed(self.nodes)):
            self.assertIs(key, value)

    def test_prepend_empty_list_prepend_node_is_head(self):
        node_string = SinglyNode('head')
        linkedlist = SinglyLinkedList()

        linkedlist.append(node_string)

        self.assertEqual(linkedlist.head.value, "head")

    def test_prepend_valid_list_prepend_node_is_head(self):
        pass

    def test_append_empty_list_append_node_is_head(self):
        node = SinglyNode('head')
        linkedlist = SinglyLinkedList()

        linkedlist.append(node)

        self.assertIs(linkedlist.head, node)

    def test_append_empty_list_append_node_is_tail(self):
        node = SinglyNode('head')
        linkedlist = SinglyLinkedList()

        linkedlist.append(node)

        self.assertIs(linkedlist.tail, node)

    def test_append_valid_list_append_node_is_tail(self):
        node = SinglyNode('tail')
        self.linkedlist.append(node)

        self.assertIs(self.linkedlist.tail, node)
