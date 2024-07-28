class TreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node with the specified data
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    # Helper function to insert a node in the correct position
    def _insert_recursive(self, node: TreeNode, data: int):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    # Inorder traversal (left, root, right)
    def inorder(self, node: TreeNode):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    # Preorder traversal (root, left, right)
    def preorder(self, node: TreeNode):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder traversal (left, right, root)
    def postorder(self, node: TreeNode):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    # Delete a node with the specified data
    def delete(self, data):
        self.root = self.delete_recursive(self.root, data)

    # Helper function for node deletion
    def delete_recursive(self, node: TreeNode, data: int):
        if node is None:
            return node
        
        # Traverse the tree to find the node to be deleted
        if data < node.data:
            node.left = self.delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self.delete_recursive(node.right, data)
        else:
            # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get the inorder successor (smallest in the right subtree)
            min_larger_node = self.min_value_node(node.right)
            node.data = min_larger_node.data
            node.right = self.delete_recursive(node.right, min_larger_node.data)
        
        return node
    # Helper function to find the node with the minimum value
    def min_value_node(self, node: TreeNode):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
# Example:
tree = BinaryTree()

# Insert nodes
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

# Traversals
print("Inorder Traversal: ", end="")
tree.inorder(tree.root)  
print()

print("Preorder Traversal: ", end="")
tree.preorder(tree.root)  
print()

print("Postorder Traversal: ", end="")
tree.postorder(tree.root)  
print()

# Delete a node
print("Deleting 5...")
tree.delete(5)

# Traversals after deletion
print("Inorder Traversal after deletion: ", end="")
tree.inorder(tree.root) 
print()

 
    
