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
        self.fixTree(node)


    def fixTree(self, node):
        while node.parent is not None and node.parent.red == True:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.red:
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.red:
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.left_rotate(node.parent.parent)
        self.root.red = False

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

    def search(self, key):
        if self.root is not None:
            currentNode = self.root
            while currentNode.key != None and key != currentNode.key:
                if key < currentNode.key:
                    currentNode = currentNode.left
                else:
                    currentNode = currentNode.right
            return currentNode
        else:
            print("Невозможно найти элемент: дерево пустое")

    def FindNext(self, x):
        current = self.search(x)
        if current:
            current = current.right
            if current.key is not None:
                while (current.left.key is not None):
                    current = current.left
                return current
        else:
            print('Данный элемент отсутсвует в дереве')

    def FindPrev(self, x):
        current = self.search(x)
        if current:
            current = current.left
            if current.key is not None:
                while (current.right.key is not None):
                    current = current.right
                return current
        else:
            print('Данный элемент отсутствует в дереве')

    def deleteNode(self, key):
        currentNode = self.search(key)
        if currentNode is self.root:
            self.delete_root_node(currentNode)
        else:
            if currentNode.key is not None:
                if currentNode == currentNode.parent.left:
                    self.delete_left_node(currentNode)
                elif currentNode.left.key is None and currentNode.right.key is not None:
                    self.delete_left_node_onlyRightChildren(currentNode)
            else:
                print("Невозможно удалить: данный узел не существует")

    def delete_root_node(self, currentNode):
        if currentNode.left.key is None and currentNode.right.key is None:
            self.root = None
        elif currentNode.left.key is None and currentNode.right.key is not None:
            self.root = currentNode.right
            currentNode.right.parent = None
        elif currentNode.left.key is not None and currentNode.right.key is None:
            self.root = currentNode.left
            currentNode.left.parent = None
        else:
            next = self.FindNext(currentNode.key)
            next.parent = None
            self.root = next
            currentNode.left.parent = self.root
            self.root.left = currentNode.left
        self.root.red = False

    def delete_left_node(self, currentNode):
        if currentNode.left.key is None and currentNode.right.key is None:
            self.delete_left_node_noChildren(currentNode)
        elif currentNode.left.key is None and currentNode.right.key is not None:
            self.delete_left_node_onlyRightChildren(currentNode)
        elif currentNode.left.key is not None and currentNode.right.key is None:
            self.delete_left_node_onlyLeftChildren(currentNode)

    def delete_left_node_noChildren(self, currentNode):
        currentNode.parent.left = currentNode.left
        currentNode.left.parent = currentNode.parent
        if currentNode.red is False:
            brother = currentNode.parent.right
            if brother.red == False:
                if brother.left.red and brother.right.red:
                    brother.right.red = False
                    self.left_rotate(brother.parent)
                elif brother.left.red and brother.right.red == False:
                    brother.left.red = False
                    brother.red = True
                    self.right_rotate(brother)
                    self.left_rotate(brother.parent.parent)
                elif brother.right.red and brother.left.red == False:
                    brother.right.red = False
                    self.left_rotate(brother.parent)
            else:
                if brother.left.key is not None and brother.right.key is not None:
                    brother.red = False
                    brother.left.red = True
                    self.left_rotate(brother.parent)

    def delete_left_node_onlyRightChildren(self, currentNode):
        currentNode.parent.left = currentNode.right
        currentNode.right.parent = currentNode.parent
        if currentNode.red is False:
            if currentNode.right.red:
                currentNode.right.red = False
        else:
            brother = currentNode.parent.right
            if brother.red == False:
                if brother.left.red and brother.right.red:
                    brother.right.red = False
                    self.left_rotate(brother.parent)
                elif brother.left.red and brother.right.red == False:
                    brother.left.red = False
                    brother.red = True
                    self.right_rotate(brother)
                    self.left_rotate(brother.parent.parent)
                elif brother.right.red and brother.left.red == False:
                    brother.right.red = False
                    self.left_rotate(brother.parent)
            else:
                if brother.left.key is not None and brother.right.key is not None:
                    brother.red = False
                    brother.left.red = True
                    self.left_rotate(brother.parent)

    def delete_left_node_onlyLeftChildren(self, currentNode):
        currentNode.parent.left = currentNode.left
        currentNode.left.parent = currentNode.parent
        if currentNode.red is False:
            if currentNode.left.red:
                currentNode.left.red = False


