class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, TreeNode):
    if root is None:
        root = TreeNode
    elif root.left is None:
        root.left = TreeNode
    elif root.right is None:
        root.right = TreeNode
    else:
        insert(root.left, TreeNode)
    return root

def create_binary_tree(values):
    root = None
    for value in values:
        new_node = TreeNode(value)
        root = insert(root, new_node)
    return root





