# Data Structure in Python by Youngsup Kim, idebtor@gmail.com 
# 2021.12.15 

class Node():
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "Node({})".format(self.key)
    
    def __len__(self):
        return sum(1 for _ in iter(self))

    def __iter__(self):
        """iterate through the nodes in the binary tree in level-order"""
        curr_nodes = [self]

        while len(curr_nodes) > 0:
            next_nodes = []
            for node in curr_nodes:
                yield node
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            curr_nodes = next_nodes
    
    def __str__(self):
        lines = self._build_tree_string(0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))
    
    def _build_tree_string(root, curr_index, include_index = False, delimiter = "-"):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.key)
        else:
            node_repr = str(root.key)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = Node._build_tree_string(
            root.left, 2 * curr_index + 1, include_index, delimiter
        )
        r_box, r_box_width, r_root_start, r_root_end = Node._build_tree_string(
            root.right, 2 * curr_index + 2, include_index, delimiter
        )

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(" " * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end
    
if __name__ == '__main__':
    root = Node(99)
    root.left = Node('A')
    root.right = Node('B')
    root.right.left = Node('E')
    root.right.right = Node('F')
    
    print(list(root))
    print('len: ', len(root))
    print('level-order by __iter__: ')
    for node in root:
        print(node.key)
        
    print(root)
