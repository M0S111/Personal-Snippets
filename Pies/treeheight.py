class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []


def makeTree(parents):
    # Create an array to store the reference
    # of all newly created nodes corresponding
    # to node value
    ref = []

    # Create n new tree nodes, each having
    # a value from 0 to n-1, and store them in ref
    for i in range(len(parents)):
        temp = TreeNode(i)
        ref.append(temp)

    # Traverse the parent array and build the tree
    for i in range(len(parents)):
        if parents[i] == -1:
            # If the parent is -1, set the root
            root = ref[i]
        else:
            # Link the current node (ref[i]) to its parent (ref[parent[i]])
            ref[parents[i]].children.append(ref[i])

    # Return the root of the newly constructed tree
    return root

        
input_list = [1,-1,1,2,2,0]
tree_root = makeTree(input_list)
#print(makeTree(input_list))

def print_tree(node, depth=0):
    if node:
        print("  " * depth + str(node.data))
        for child in node.children:
            print_tree(child, depth + 1)

print_tree(tree_root)

def tree_height(root):
    if not root:
        return 0  # Base case: an empty tree has height 0

    # Recursively find the height of each child
    child_heights = [tree_height(child) for child in root.children]

    # The height of the tree is 1 + the maximum height of its children
    return 1 + (max(child_heights) if child_heights else 0)

print(tree_height(tree_root))
