import helper


def BFS_knearest_distance(graph, start, k):
    queue = []
    queue.append([start])
    marked = [False] * (max(graph.keys()) + 1)
    marked[start] = True

    # Create a list to store hospital nodes
    hospital_list = []
    # Create a list to store distance from source node
    distance = [0] * (max(graph.keys()) + 1)

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path. This will be checked if
        # it is a hospital, and if not it will be checked for neighbouring
        # nodes in the for loop later to append into the queue.
        node = path[-1]
        # Search next node if next node is a hospital
        if 'h' in graph[node]:
            hospital_list.append([start, distance[node], node])
            if len(hospital_list) == k:
                return hospital_list
        # Create a list of each neighbouring node to the last node
        # in our current search path and append to the queue
        for adjacent in graph[node]:
            if adjacent == 'h':
                continue
            # If item has been searched do not append to queue
            elif marked[adjacent]:
                continue

            distance[adjacent] = distance[node] + 1
            # to_queue will take in the current path and one adjacent
            # node will be appended to it. This is done in the for loop
            # to add every single unexplored neighbouring node.
            to_queue = list(path)
            to_queue.append(adjacent)
            marked[adjacent] = True
            queue.append(to_queue)
    return hospital_list



############################################################################################
#############                          SMALL GRAPH                          #################
############################################################################################
small_graph = helper.add_graph('./input/small_graph.txt')
small_graph = helper.add_hospitals(small_graph, './input/small_hospital.txt')
K = 3

# Find nearest hospital to every node and write the Hospital Node,
# Distance and Path to text file small_graph_Q1_C_D.txt
f = open("./output/small_graph_Q1_C_D.txt", "w")
f.write("K = " + str(K) + "\n\n")
for key in small_graph.keys():
    to_write = BFS_knearest_distance(small_graph, key, K)

    print("Searching Node", key, "...")

    f.write("Starting Node: " + str(key) + "\n")
    # Node is not connected to any hospital nodes.
    if not to_write:
        print("Nearest Hospital at: N/A")
        print("Distance: N/A")
        print("Path: N/A")

        f.write("Nearest Hospital at: N/A\n")
        f.write("Distance: N/A\n")
        f.write("Path: N/A\n\n")
    # Node is connected to some hospital nodes (or K number).
    else:
        for item in to_write:
            print("Nearest Hospital at:", item[-1])
            print("Distance:", item[1])

            f.write("Nearest Hospital at: " + str(item[-1]) + "\n")
            f.write("Distance: " + str(item[1]) + "\n")
    f.write("\n")
    print()
f.close()
print("Output is written to text file small_graph_Q1_C_D.txt...\n")

# ############################################################################################
# #############                          LARGE GRAPH                          ################
# ############################################################################################
large_graph = helper.add_graph('./input/large_graph.txt')
helper.create_hospitals(large_graph, './input/large_hospital.txt')
large_graph = helper.add_hospitals(large_graph, './input/large_hospital.txt')
K = 3

# Find nearest hospital to every node and write the Hospital Node,
# Distance and Path to text file large_graph_Q1_C_D.txt

f = open("./output/large_graph_Q1_C_D.txt", "w")
f.write("K = " + str(K) + "\n\n")
for key in large_graph.keys():
    to_write = BFS_knearest_distance(large_graph, key, K)

    print("Searching Node", key, "...")

    f.write("Starting Node: " + str(key) + "\n")
    # Node is not connected to any hospital nodes.
    if not to_write:
        print("Nearest Hospital at: N/A")
        print("Distance: N/A")
        print("Path: N/A")

        f.write("Nearest Hospital at: N/A\n")
        f.write("Distance: N/A\n")
        f.write("Path: N/A\n\n")
    # Node is connected to some hospital nodes (or K number).
    else:
        for item in to_write:
            print("Nearest Hospital at:", item[-1])
            print("Distance:", item[1])

            f.write("Nearest Hospital at: " + str(item[-1]) + "\n")
            f.write("Distance: " + str(item[1]) + "\n")
    f.write("\n")
    print()
f.close()
print("Output is written to text file large_graph_Q1_C_D.txt...\n")









