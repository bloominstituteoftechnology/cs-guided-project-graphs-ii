#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def treePaths(root):
    '''
    Input: the root of the tree to traverse 
    Output: list of strings where a single string 
    represents a single path through the tree 
    
    Since we are looking to enumerate all of the paths,
    a depth-first traversal would work well for this.
    
    Let's implement our DFT recursively.
    What are our base cases?
    1. When we encounter a leaf node, we're done building 
       up the current path. Add the current path to our 
       answer list (reformat the path as a string)
    How do we get closer to a base case? 
    1. Add the current node's value to the current path that 
       we're building up, and then recursively traverse down to
       the node's children.
    
    Every time we pass control back up the recursion stack, 
    we need to pop the latest value from the current path 
    that we're building up 
    '''
    result = [] 
    dft(root, [], result)
    
    return result 
    
# Define a new recursive function with the signature
# we need since the original function doesn't have 
# the signature we need 
def dft(node, current_path, result):
    # base case
    # if the current node is None 
    if not node:
        return
        
    # turn the node value into a string 
    # before appending it to the current path 
    current_path.append(f'{node.value}')
    
    # when the current node is a leaf 
    if is_leaf(node):
        # after adding the current node's value to the path list
        # take the current path and add it to our result list 
        # append a snapshot of the current path at this
        # point in time to the result list 
        result.append("->".join(current_path[:]))
    
    # otherwise, add the current node's value to the path list
    
    # make further recursive calls to this node's children 
    dft(node.left, current_path, result)
    dft(node.right, current_path, result)
    # pop the last element from the current path 
    current_path.pop()
    
def is_leaf(node):
    return node.left is None and node.right is None