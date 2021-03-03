class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        """Iterate through all left possibilities, return min"""
        while self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        """Iterate through all right possibilities, return min"""
        while self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        """Calculate sum of all nodes in BST"""
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self, val):
        """Delete node of specific value"""
        if val < self.data:
            # search left subtree
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            # search right subtree
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # Case where there are more subtrees
            # Copy min from right subtree
            min_val = self.right.find_min()
            self.data = min_val
            # Delete duplicate node
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for x in range(1, len(elements)):
        root.add_child(elements[x])

    return root


if __name__ == "__main__":
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    print("Building tree...")
    nums_tree = build_tree(nums)
    print(nums_tree.in_order_traversal())
    print(nums_tree.search(20))
    print("Deleting node...")
    nums_tree.delete(20)
    print(nums_tree.in_order_traversal())
