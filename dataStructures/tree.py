class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Add a TreeNode to the Tree"""
        # Make the child's parent equal to main TreeNode
        # Add treenode to tree
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """Tells you the level of the passed node"""
        # Count amount of ancestors (parents)
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        """Go through children 1 by 1 and print data"""
        prefix = " " * self.get_level() * 3
        prefix += "|__" if self.parent else ""
        print(prefix + self.data)
        # Check if we are at a leaf node
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    """Build product tree for electronic items"""
    # Parent node
    root = TreeNode("Electronics")

    # Create child node and children
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    # Add laptop, cellphone, tv as children of "Electronics"
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass
