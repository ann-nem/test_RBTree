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

    #поиск узлов в дереве
    def test_find_node(self):
        rb_tree = RBtree()
        rb_tree.insert(2)
        node_2 = rb_tree.root
        rb_tree.insert(1)
        node_1 = rb_tree.root.left
        rb_tree.insert(4)
        node_4 = rb_tree.root.right
        rb_tree.insert(5)
        node_5 = node_4.right
        rb_tree.insert(9)
        node_9 = node_5.right
        rb_tree.insert(3)
        node_3 = node_4.left
        rb_tree.insert(6)
        node_6 = node_9.left
        rb_tree.insert(7)
        node_7 = node_5.right
        rb_tree.insert(15)
        node_15 = node_9.right

        self.assertEqual(rb_tree.search(5), node_5)
        self.assertEqual(rb_tree.search(2), node_2)
        self.assertEqual(rb_tree.search(1), node_1)
        self.assertEqual(rb_tree.search(4), node_4)
        self.assertEqual(rb_tree.search(3), node_3)
        self.assertEqual(rb_tree.search(7), node_7)
        self.assertEqual(rb_tree.search(6), node_6)
        self.assertEqual(rb_tree.search(9), node_9)
        self.assertEqual(rb_tree.search(15), node_15)

    #вставка узлов дерева
    def test_Insert(self):
        tree = RBtree()
        tree.insert(20)
        tree.insert(15)
        tree.insert(25)
        tree.insert(10)

        self.assertEqual(tree.root.red, False)
        self.assertEqual(tree.search(15).red, False)
        self.assertEqual(tree.search(25).red, False)
        tree.insert(17)
        tree.insert(8)
        self.assertEqual(tree.search(15).red, True)
        self.assertEqual(tree.search(10).red, False)
        self.assertEqual(tree.search(17).red, False)
        self.assertEqual(tree.search(8).red, True)
        tree.insert(9)
        self.assertEqual(tree.search(10).red, True)
        self.assertEqual(tree.search(8).red, True)
        self.assertEqual(tree.search(9).left.key, 8)

