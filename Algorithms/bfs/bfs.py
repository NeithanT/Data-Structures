
"""
    Implementation for Breadth-First Search (BFS) algorithm in Python.

    Note that having a collection of visited nodes is crucial, 
    because of cycles in graphs.

    In trees, this is not a concern since there are no cycles

    Uses a queue to keep track of nodes.
"""
def breadth_first_search(graph, start):

    # A set or dictionary.
    visited = {}

    queue = [start]

    # The order in which nodes are visited.
    order = []

    # while there are nodes in the tree/graph
    while queue:

        # Get the first node,
        # This was added the earliest
        # So it basically goes layer by layer

        node = queue.pop(0)

        # This will not be necessary if it was a tree
        if node not in visited:


            visited.add(node)
            order.append(node)

            for neighbor in graph[node]:
                # You could also add a condition here if you are searching for a node
                # if neighbor == target:
                #     found = True
                
                if neighbor not in visited:
                    queue.append(neighbor)
                # Alternatively, using list comprehension
                # queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

        

    return order
