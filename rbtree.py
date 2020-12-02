class Node:
    def __init__(self, key):
        self.key = key
        self.red = True
        self.right = None
        self.left = None
        self.parent = None


class RBtree(Node):

    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        node.red = True

        #вставка корня дерева
        if self.root == None:
            node.red = False
            self.root = node
            node.left = Node(None)
            node.left.red = False
            node.right = Node(None)
            node.right.red = False
            return
