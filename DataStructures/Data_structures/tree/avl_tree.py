class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  


class AVLTree:
    def insert(self, root, key):
        # Perform normal BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Check for imbalance and perform rotations if needed
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, node):
        return node.height if node else 0

    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    def preOrder(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


# Example usage:
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25] 

    for key in keys:
        root = avl.insert(root, key)

    print("Pre-order traversal of the constructed AVL tree is:")
    avl.preOrder(root)
