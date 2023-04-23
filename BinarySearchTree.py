from typing import List
from BinaryTree import TreeNode

class BinarySearchT:
    def __init__(self, values: List[int]):
        self.root = None
        for value in values:
            self.insert(value)

    def insert(self, value: int) -> None:
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def convert_to_bst(self) -> TreeNode:
        values = []
        self.get_values(self.root, values)
        return self.create_bst(values, 0, len(values) - 1)

    def get_values(self, root: TreeNode, values: List[int]) -> None:
        if root is None:
            return
        self.get_values(root.left, values)
        values.append(root.value)
        self.get_values(root.right, values)

    def create_bst(self, values: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(values[mid])
        root.left = self.create_bst(values, start, mid - 1)
        root.right = self.create_bst(values, mid + 1, end)
        return root

    def print_in_order(self, root: TreeNode) -> None:
        if root:
            self.print_in_order(root.left)
            print(root.value)
            self.print_in_order(root.right)






