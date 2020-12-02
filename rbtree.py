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

        currentNode = self.root
        while currentNode.key != None:
            potentialParent = currentNode
            if node.key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            node.parent = potentialParent
        if node.key < node.parent.key:
            currentNode.left = node
            node.parent.left = node
        else:
            currentNode.right = node
            node.parent.right = node
        node.left = Node(None)
        node.left.red = False
        node.right = Node(None)
        node.right.red = False
        #self._fixTree(node)

    def left_rotate(self, node):
        sibling = node.right
        node.right = sibling.left
        if sibling.left != None:
            sibling.left.parent = node
        sibling.parent = node.parent
        if node.parent == None:
            self.root = sibling
        else:
            if node == node.parent.left:
                node.parent.left = sibling
            else:
                node.parent.right = sibling
        sibling.left = node
        node.parent = sibling

    def right_rotate(self, node):
        sibling = node.left
        node.left = sibling.right
        if sibling.right != None:
            sibling.right.parent = node
        sibling.parent = node.parent
        if node.parent == None:
            self.root = sibling
        else:
            if node == node.parent.right:
                node.parent.right = sibling
            else:
                node.parent.left = sibling
        sibling.right = node
        node.parent = sibling
