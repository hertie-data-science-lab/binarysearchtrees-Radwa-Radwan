class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, TreeNode):
    if root is None:
        root = TreeNode
    elif TreeNode.value < root.value:
        root.left = insert(root.left, TreeNode)
    else:
        root.right = insert(root.right, TreeNode)
    return root

def create_binary_tree(values):
    root = None
    for value in values:
        new_node = TreeNode(value)
        root = insert(root, new_node)
    return root






