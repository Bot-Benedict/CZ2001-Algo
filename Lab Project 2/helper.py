import csv
import networkx as nx
import numpy as np
from random import randrange
import random

def set_seed():
    """
    Sets seed as several other functions like create_hospitals uses random.
    :return:
    """
    random.seed(30)
    np.random.seed(30)


def create_hospitals(graph, directory):
    """
    Randomly assigns between 1 to 1/3 of total number of nodes as a hospital.
    Hospital nodes are assigned in the dictionary value itself. This allows for a better
    average case time complexity (O(1)) as compared to storing information of hospitals in
    a list which takes O(n).

    However, as a result the other functions created will have to accomodate to ignore 'h' as it is not a node.

    Parameters
    ----------
    graph : dictionary
        Dictionary containing the node as key and all edges as values.
    num_nodes : int
        Total number of nodes in the graph.
    """
    set_seed()
    num_hospitals = randrange(1, int((len(graph) / 3) + 1))
    hospital_nodes = random.sample(graph.keys(), num_hospitals)
    f = open(directory, 'w')
    f.write('#'+str(len(hospital_nodes))+"\n")
    for node in hospital_nodes:
        f.write(str(node)+"\n")
    f.close()


def add_graph(graph_txt):
    """
    Reads a text file and creates a graph of it.
    :param graph_txt: Directory to text file of graph.
    :return: Dictionary containing start nodes as key and its neighbouring nodes as value.
    """
    # read input graph text file
    with open(graph_txt) as f:
        reader = csv.reader(f, delimiter="\t")
        item = list(reader)

    # create dictionary values with empty array
    graph = {}
    for nodes in item[4:]:
        graph[int(nodes[0])] = []

    for nodes in item[4:]:
        graph[int(nodes[0])].append(int(nodes[1]))

    return graph


def add_hospitals(graph, hospital_txt):
    """
    Reads a text file containing the hospital nodes and add to graph.

    :param graph: Dictionary containing start nodes as key and its neighbouring nodes as value.
    :param hospital_txt: Directory to hospital text file.
    :return: Updated graph with hospital information.
    """
    # read input hospital file
    with open(hospital_txt) as f:
        reader = csv.reader(f, delimiter="\t")
        item = list(reader)

    # add hospital to graph dictionary
    for hospital_nodes in item[1:]:
        graph[int(hospital_nodes[0])].append('h')

    return graph


def draw_graph(graph):
    """
    Creates a networkx graph for visualization purposes only.
    Hospitals are colored red while normal nodes are colored green.

    :param graph: Dictionary containing start nodes as key and its neighbouring nodes as value.
    :return:
    """
    g = nx.Graph(graph)
    node_colors = ['g'] * (len(g) - 1)
    for node in g:
        for edge in g.edges(node):
            if edge[1] == 'h':
                node_colors[node] = 'r'
                break

    g.remove_node('h')
    nx.draw_spring(g, node_color=node_colors, with_labels=True)
