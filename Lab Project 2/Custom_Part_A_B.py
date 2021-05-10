def BFS_shortest_path(graph, start):
    """
    Finds the nearest hospital and returns the path taken from source node to nearest hospital.
    :param graph: Dictionary containing the node as key and all edges as values.
    :param start: Source node.
    :return: List containing the path from source node to nearest hospital.
    """

    queue = [[start]]
    marked = [False] * (max(graph.keys())+1)
    marked[start] = True
    
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # Hospital found at current node
        if 'h' in graph[node]:
            return path
        
        # Otherwise begin queueing adjacent nodes
        for adjacent in graph[node]:
            
            # check if adjacent ='h' as our dictionary does not have a key value 'h'
            if adjacent == 'h' or marked[adjacent]:
                continue
                
            # create a path from existing path to current adjacent node and mark adjacent
            # node as explored.
            to_queue = list(path)
            to_queue.append(adjacent)
            marked[adjacent] = True
            
            # before enqueueing, check if adjacent node has a hospital. If yes return the path.
            if 'h' in graph[adjacent]:
                return to_queue
            queue.append(to_queue)
    return []

import helper
custom_graph = helper.add_graph('./input/small_graph.txt')
helper.create_hospitals(custom_graph, './input/custom_hospital.txt')
custom_graph = helper.add_hospitals(custom_graph, './input/custom_hospital.txt')

# Find nearest hospital to every node and write the Hospital Node,
# Distance and Path to text file custom_graph_Q1_A_B.txt
f = open("./output/custom_graph_Q1_A_B.txt", "w")
for key in custom_graph.keys():
    to_write = BFS_shortest_path(custom_graph, key)

    print("Starting Node:", key)
    f.write("Starting Node: " + str(key) + "\n")

    # Node is not connected to any hospital nodes
    if not to_write:
        print("Nearest Hospital at: N/A")
        print("Distance: N/A")
        print("Path: N/A")

        f.write("Nearest Hospital at: N/A\n")
        f.write("Distance: N/A\n")
        f.write("Path: N/A\n\n")

    # Node is connected to hospital node.
    else:
        print("Nearest Hospital at:", str(to_write[-1]))
        print("Distance:", str(len(to_write) - 1))
        print("Path:", str(to_write))

        f.write("Nearest Hospital at: " + str(to_write[-1]) + "\n")
        f.write("Distance: " + str(len(to_write) - 1) + "\n")
        f.write("Path: " + str(to_write) + "\n\n")

    print()
f.close()
print("Output is written to text file custom_graph_Q1_A_B.txt...\n")