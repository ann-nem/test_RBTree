import unittest
from rbtree import RBtree, Node


class RbTreeTests(unittest.TestCase):

    #инициализация дерева
    def test_tree_init(self):
        rb_tree = RBtree()
        self.assertIsNone(rb_tree.root, None)

    #инициализация узла дерева
    def test_node_init(self):
        node = Node(15)
        self.assertEqual(node.key, 15)
        self.assertTrue(node.red)
        self.assertIsNone(node.right, None)
        self.assertIsNone(node.left, None)
        self.assertIsNone(node.parent, None)

    #вставка корня дерева
    def test_insert_root(self):
        rb_tree = RBtree()
        rb_tree.insert(15)
        self.assertEqual(rb_tree.root.key, 15)
        self.assertEqual(rb_tree.root.key, 15)