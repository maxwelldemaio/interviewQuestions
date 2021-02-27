import typing

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, treeType: str) -> None:
        """Go through children 1 by 1 and print data"""
        nameDesStr = " " * self.get_level() * 3
        nameDesStr += "|__" if self.parent else ""
        # Based on passed treeType, output tree
        if treeType == "name":
            nameDesStr += self.name
        elif treeType == "designation":
            nameDesStr += self.designation
        else:
            nameDesStr += self.name + " " + self.designation

        print(nameDesStr)
        # Check if we are at a leaf node
        if self.children:
            for child in self.children:
                child.print_tree(treeType)
        return


def build_management_tree():
    """Build product tree for electronic items"""
    # Parent node
    root = TreeNode("Nilupul", "CEO")

    # Create child node and children
    tech = TreeNode("Chinmay","CTO")
    infra = TreeNode("Vishwa", "Infrastructure Head")
    tech.add_child(infra)
    infra.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra.add_child(TreeNode("Abhijit", "App Manager"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "iPhone Head"))

    # Add infra and hr as children of management tree
    root.add_child(infra)
    root.add_child(hr)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    # prints both (name and designation) hierarchy
    root_node.print_tree("both")
