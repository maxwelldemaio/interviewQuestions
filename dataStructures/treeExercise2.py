import typing


class TreeNode:
    def __init__(self, location):
        self.location = location
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

    def print_tree(self, level: int):
        """Go through children 1 by 1 and print data"""
        currLevel = self.get_level()
        prefix = " " * currLevel * 3
        prefix += "|__" if self.parent else ""
        print(prefix + self.location)
        # Only print children of node if self.get_level is >= than level
        # Check if we are at a leaf node
        if level > currLevel:
            if self.children:
                for child in self.children:
                    child.print_tree(level)


def build_location_tree():
    """Build location tree"""
    # Parent node
    root = TreeNode("Global")

    # Create child node and children
    usa = TreeNode("USA")
    nj = TreeNode("New Jersey")
    cali = TreeNode("California")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))
    cali.add_child(TreeNode("San Francisco"))
    cali.add_child(TreeNode("Mountain View"))
    cali.add_child(TreeNode("Palo Alto"))
    usa.add_child(nj)
    usa.add_child(cali)

    india = TreeNode("India")
    guj = TreeNode("Gujarat")
    karna = TreeNode("Karnataka")

    guj.add_child(TreeNode("Ahmedabad"))
    guj.add_child(TreeNode("Baroda"))
    karna.add_child(TreeNode("Bangluru"))
    karna.add_child(TreeNode("Mysore"))
    india.add_child(guj)
    india.add_child(karna)

    # Add usa and india as children of location tree
    root.add_child(usa)
    root.add_child(india)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)  # prints only name hierarchy
