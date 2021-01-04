def csFindAllPathsFromAToB(graph):
    '''
    Input: a graph represented as an adjacency list 
    Output: a list of lists of all the 
    possible paths through the graph 
    '''
    
    result = [] 
    
    dft(graph, 0, [0], result)
    
    return result 
    
def dft(graph, current_node, current_path, result):
    # base case
    # when we finish traversing through our graph 
    if current_node == len(graph) - 1:
        result.append(current_path[:])
    # how do we know when to add the path to the result list 
    # if a node has no outgoing connections, then we'll add the current_path to the result list 
    # how do we get closer to a base case? 
    # iterate over all of the current graph node's 
    # connections; recurse on every single one of them 
    connections = graph[current_node]
    
    for connection in connections:
        # add the connection to our current_path 
        current_path.append(connection)
        dft(graph, connection, current_path, result)
        # pop off the end of our current path 
        current_path.pop()