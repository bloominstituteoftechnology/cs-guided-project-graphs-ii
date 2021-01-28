class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return f"GraphNode({repr(self.value)})"

# Build this by hand here
a = GraphNode("A")
b = GraphNode("B")
c = GraphNode("C")
d = GraphNode("D")
e = GraphNode("E")
f = GraphNode("F")
g = GraphNode("G")

a.edges = [c, d, b]
b.edges = [e, a]
c.edges = [d]
d.edges = [f, e]
e.edges = [f]
f.edges = [g]

from collections import deque

def bft(starting_node):
    # Init: add the first node to the queue
    queue = deque()
    queue.append(starting_node)  # enqueue

    # Keep track of visited nodes
    visited = set()

    # Loop while queue isn't empty
    while len(queue) != 0:
        # dequeue first node
        n = queue.popleft()   # dequeue
        
        # if already visited: continue
        if n in visited:
            continue

        # visit it
        print(n.value)

        # add to visited set
        visited.add(n)

        # enqueue all the neighbors
        for neighbor in n.edges:
            queue.append(neighbor)   # enqueue

bft(a)

def bfs(starting_node, ending_node):
    # Keep track of paths so far
    paths = {}

    # Init: add the first node to the queue
    queue = deque()
    queue.append(starting_node)  # enqueue

    paths[starting_node] = [starting_node.value]

    # Keep track of visited nodes
    visited = set()

    # Loop while queue isn't empty
    while len(queue) != 0:
        # dequeue first node
        n = queue.popleft()   # dequeue
        
        # if already visited: continue
        if n in visited:
            continue

        # visit it
        #print(n.value, paths[n])

        # add to visited set
        visited.add(n)

        # enqueue all the neighbors
        for neighbor in n.edges:
            # Update path to this neighbor
            """
            path_to_n = paths[n]
            path_to_neighbor = path_to_n + [neighbor.value]
            paths[neighbor] = path_to_neighbor
            """

            if neighbor not in paths:
                paths[neighbor] = paths[n] + [neighbor.value]

            # These are the droids we're looking for
            if neighbor == ending_node:
                return paths[neighbor]

            #print(f"Going from {n.value} to {neighbor.value}")

            queue.append(neighbor)   # enqueue
            #print(f"queue: {queue}")

        # If we got here, didn't find anything
        return None

print(bfs(a,a))  # shortest path from a to f