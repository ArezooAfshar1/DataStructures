class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_rec(self.root, data)

    # Helper method to insert recursively.
    def _insert_rec(self, current_node, data):
        
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_rec(current_node.left, data)
        elif data > current_node.data:  
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_rec(current_node.right, data)

    # Search for a data in the BST
    def search(self, data):
        return self._search_rec(self.root, data)

    # Helper method to search recursively
    def _search_rec(self, node, data):
        if node is None or node.data == data:
            return node
        return self._search_rec(node.left, data) if data < node.data else self._search_rec(node.right, data)

    # Return the inorder traversal of the BST.
    def inorder(self):
        return self._inorder_rec(self.root)

    # "Helper method to perform inorder traversal recursively.
    def _inorder_rec(self, node):
        if node is None:
            return []
        return self._inorder_rec(node.left) + [node.data] + self._inorder_rec(node.right)

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)  

print("Inorder traversal:", bst.inorder()) 
print("Searching for 7:", bst.search(7) is not None)  
print("Searching for 10:", bst.search(10) is not None)  
