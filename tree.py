class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def perfect_tree_sum(root):
    if root is None:
        return 0

    height = 0
    node = root
    while node is not None:
        height += 1
        node = node.left

    return (2 ** height) - 1

# Example usage
if __name__ == '__main__':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    print("Sum of all nodes: ", perfect_tree_sum(root))