class Node:
    def __init__(self, value, color, left=None, right=None, parent=None):
        self.value = value
        self.color = color  # "red" or "black"
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.null = Node(None, "black")
        self.root = self.null

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.null:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.null:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def insert(self, key):
        node = Node(key, "red", left=self.null, right=self.null)
        parent = None
        curr = self.root
        while curr != self.null:
            parent = curr
            if node.value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                uncle = k.parent.parent.left
                if uncle.color == "red":
                    uncle.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                uncle = k.parent.parent.right
                if uncle.color == "red":
                    uncle.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
        self.root.color = "black"
