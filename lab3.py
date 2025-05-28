class BinaryTree: 
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    tree.left, tree.right = tree.right, tree.left

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

    return tree

def print_tree(tree):
    if tree is None:
        return []
    result = []
    queue = [tree]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# Тест
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

inverted = invert_binary_tree(root)

print(print_tree(inverted))  # Очікується: [1, 3, 2, 7, 6, 5, 4]
