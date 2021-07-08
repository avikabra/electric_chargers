import csv
from operator import itemgetter
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt


####################################################################################################################
# READING REQUIRED CSV FILES AND CONVERTING THEM INTO LISTS/DICTIONARIES

# DISTRIBUTION NETWORK
print('DISTRIBUTION NETWORK')
#To print the list of names of nodes:
with open(r'data/distribution_nodes.csv', 'r') as dist_nodecsv: # Open the file
    dist_nodereader = csv.reader(dist_nodecsv) # Read the csv
    dist_nodes = [n for n in dist_nodereader][1:]
dist_node_names = [n[0] for n in dist_nodes] # Get a list of only the node names
#print('List of all the nodes of the distribution network:', dist_node_names)
#print()

#To print the list of edges in the form of ordered pairs:
with open(r'data/distribution_edges.csv', 'r') as dist_edgecsv: # Open the file
    dist_edgereader = csv.reader(dist_edgecsv) # Read the csv
    dist_edges = [tuple(e) for e in dist_edgereader][1:] # Retrieve the data
#print('List of all the edges in the network:', dist_edges)
#print()

#To print the list of positions of the nodes on the Cartesian plane:
with open(r'data/distribution_pos.csv', 'r') as dist_poscsv:
    dist_posreader = csv.reader(dist_poscsv)
    dist_pos = [tuple(e) for e in dist_posreader][1:]
#print('List of all the positions to be assigned to the nodes of distribution network:', dist_pos)


#Assigning the positions to specific nodes in a dictionary (final_pos)
dist_pos = [(float(x), float(y)) for (x,y) in dist_pos]
final_pos1 = {}
for i in dist_node_names:
    for j in dist_pos:
        final_pos1[i] = j
        dist_pos.remove(j)
        break
#print('Assigned positions to the nodes of distribution network:', final_pos1)


#reading the file containing the corresponding stability factors
with open(r'data/distribution_nodes.csv', 'r') as VSFcsv: # Open the file
    VSFreader = csv.reader(VSFcsv) # Read the csv
    VSF = [n for n in VSFreader][1:]
VSF_names = [n[1] for n in VSF] # Get a list of only the node names
VSF_names = [ float(x) for x in VSF_names]
#print('List of all the nodes of the network:', VSF_names)
#print()

stability_factors = {}
for i in dist_node_names:
    for j in VSF_names:
        stability_factors[i] = j
        VSF_names.remove(j)
        break
print('Assigning stability factors to the corresponding edges:', stability_factors)
print()
#ROAD NETWORK

print('ROAD NETWORK')
#To print the list of names of nodes:
with open(r'data/road_nodes.csv', 'r') as road_nodecsv: # Open the file
    road_nodereader = csv.reader(road_nodecsv) # Read the csv
    road_nodes = [n for n in road_nodereader][1:]
road_node_names = [n[0] for n in road_nodes] # Get a list of only the node names
#print('List of all the nodes of the network:', road_node_names)
#print()

#To print the list of edges in the form of ordered pairs:
with open(r'data/road_edges.csv', 'r') as road_edgecsv: # Open the file
    road_edgereader = csv.reader(road_edgecsv) # Read the csv
    road_edges = [tuple(e) for e in road_edgereader][1:] # Retrieve the data
#print('List of all the edges in the network:', road_edges)
#print()

#To print the list of positions of the nodes on the Cartesian plane:
with open(r'data/road_pos.csv', 'r') as road_poscsv:
    road_posreader = csv.reader(road_poscsv)
    road_pos = [tuple(e) for e in road_posreader][1:]
#print('List of all the positions to be assigned to the nodes of transportation network:', road_pos)

#Assigning the positions to specific nodes in a dictionary (final_pos)
road_pos = [(float(x), float(y)) for (x,y) in road_pos]
final_pos2 = {}
for i in road_node_names:
    for j in road_pos:
        final_pos2[i] = j
        road_pos.remove(j)
        break
#print('Assigned positions to the nodes of transportation network:', final_pos2)


#To print the list of weights signifying traffic conditions at diff edges in float format:
with open(r'data/road_weights.csv', 'r') as weightcsv: # Open the file
    weightreader = csv.reader(weightcsv) # Read the csv
    weights = [n for n in weightreader][1:]
weights_values = [n[0] for n in weights] # Get a list of only the node names
final_weights = [ float(x) for x in weights_values]
#print('List of all the congestion factors to be assigned to the edges:', final_weights)
#print()

#Assigning the weights to specific edges in a dictionary (probabilities)
probabilities = {}
for i in road_edges:
    for j in final_weights:
        probabilities[i] = j
        final_weights.remove(j)
        break
print('Assigning congestion factors to the corresponding edges:', probabilities)
print()

with open(r'data/road_length.csv', 'r') as lengthcsv: # Open the file
    lengthreader = csv.reader(lengthcsv) # Read the csv
    lengths = [n for n in lengthreader][1:]
lengths_values = [n[0] for n in lengths] # Get a list of only the node names
final_lengths = [ float(x) for x in lengths_values]
#print('List of all the distance factors to be assigned to the edges:', final_lengths)
#print()

#Assigning the weights to specific edges in a dictionary (probabilities)
Distances = {}
for i in road_edges:
    for j in final_lengths:
        Distances[i] = j
        final_lengths.remove(j)
        break
print('Assigning distance factors to the corresponding edges:', Distances)
print()


#########################################################################################################################
#CREATING A GRAPH FOR THE REQUIRED NETWORK

G1 = nx.Graph()
G2 = nx.Graph()
#Adding nodes and edges
G1.add_nodes_from(dist_node_names)
G2.add_nodes_from(road_node_names)
G1.add_edges_from(dist_edges)
G2.add_edges_from(road_edges)

#Adding attributes
nx.set_node_attributes(G1, stability_factors, 'stability_factors')
nx.set_edge_attributes(G2, Distances, 'Distances')
nx.set_edge_attributes(G2, probabilities, 'probabilities')

#Visualization
nx.draw(G1, final_pos1, node_color="tab:red", edge_color = "tab:red", node_shape = 's')
nx.draw(G2, final_pos2, node_color="tab:blue", edge_color = "tab:blue", with_labels = True)
plt.show()

#########################################################################################################################
#CREATING A GRAPH FOR THE REQUIRED NETWORK

"""
Bayesian network structure: 
Children --> stability factor at a given node, average congestion factor of all corresponding edges, average distances factors of all corresponding edges
Parent --> Candidate (y/n)
"""

from pomegranate import *

# child dictionaries: stability_factors, probabilities, Distances
# VSF
num_nodes = len(stability_factors)

stability_probability = {}
stability_probability["low"] = 0
stability_probability["medium"] = 0
stability_probability["high"] = 0

low_thresh = (max(stability_factors.values()) - min(stability_factors.values()))/3 + min(stability_factors.values())
medium_thresh = (max(stability_factors.values()) + low_thresh)/2

# count
for node in stability_factors:
    if (stability_factors[node] < low_thresh):
        stability_probability["low"] += 1
    elif (stability_factors[node] < medium_thresh):
        stability_probability["medium"] += 1
    else:
        stability_probability["high"] += 1

# scale from 0-1
for state in stability_probability:
    stability_probability[state] /= num_nodes

# VSF with no parent
vsf = Node(DiscreteDistribution({
    "low": stability_probability["low"],
    "medium": stability_probability["medium"],
    "high": stability_probability["high"]
}), name="vsf")


# congestion factor

congestion_probabilites = {}
congestion_probabilites["low"] = 0
congestion_probabilites["high"] = 0

thresh = (min(probabilities.values()) + max(probabilities.values()))/2

# count
for node in road_node_names:
    node_sum = 0
    count = 0
    for key in probabilities:
        if node == key[0] or node == key[1]:
            node_sum += probabilities[key]
            count += 1
    if count != 0 and node_sum / count > thresh:
        congestion_probabilites["high"] += 1
    elif count != 0:
        congestion_probabilites["low"] += 1

# scale from 0-1
for state in congestion_probabilites:
    congestion_probabilites[state] /= len(road_node_names)

# congestion probability distribution with no parent
congestion = Node(DiscreteDistribution({
    "low": congestion_probabilites["low"],
    "high": congestion_probabilites["high"]
}), name="congestion")


# distance factor
distance_probabilitiy = {}
distance_probabilitiy["low"] = 0
distance_probabilitiy["medium"] = 0
distance_probabilitiy["high"] = 0

low_thresh_d = (max(Distances.values()) - min(Distances.values()))/3 + min(Distances.values())
medium_thresh_d = (max(Distances.values()) + low_thresh_d)/2

# count
for node in road_node_names:
    node_sum = 0
    count = 0
    for key in Distances:
        if node == key[0] or node == key[1]:
            node_sum += Distances[key]
            count += 1
    if count != 0 and node_sum / count < low_thresh_d:
        distance_probabilitiy["low"] += 1
    elif count != 0 and node_sum / count < medium_thresh_d:
        distance_probabilitiy["medium"] += 1
    elif count != 0:
        distance_probabilitiy["high"] += 1

# scale from 0-1
for state in distance_probabilitiy:
    distance_probabilitiy[state] /= len(road_node_names)

# VSF with no parent
distance = Node(DiscreteDistribution({
    "low": distance_probabilitiy["low"],
    "medium": distance_probabilitiy["medium"],
    "high": distance_probabilitiy["high"]
}), name="distance")


# construction of candidate data table based on following assumptions
# * 1/12 - 1/3 - 7/12 scale for 3 state child nodes, 25 - 75 for two state
# * high vsf is good, low vsf is bad | 1/12, 1/3, 7/12
# * high congestion is good, low is bad | 1/4, 3/4
# * high distance is bad, low is good | 7/12, 1/3, 1/12

# Candidate node is conditional on vsf, congestion, and distance

candidate = Node(ConditionalProbabilityTable([
    ["low", "low", "low", 7 * .25 / 144],
    ["low", "low", "medium", .25 * 4 / 144],
    ["low", "low", "high", .25 / 144],
    ["low", "high", "low", .75 * 7 / 144],
    ["low", "high", "medium", .75 * 4 / 144],
    ["low", "high", "high", .75 / 144],
    ["medium", "low", "low", 4 * 7 * .25 / 144],
    ["medium", "low", "medium", 4 * .25 * 4 / 144],
    ["medium", "low", "high", 4 * .25 / 144],
    ["medium", "high", "low", 4 * .75 * 7 / 144],
    ["medium", "high", "medium", 4 * .75 * 4 / 144],
    ["medium", "high", "high", 4 * .75 / 144],
    ["high", "low", "low", 7 * 7 * .25 / 144],
    ["high", "low", "medium", 7 * .25 * 4 / 144],
    ["high", "low", "high", 7 * .25 / 144],
    ["high", "high", "low", 7 * .75 * 7 / 144],
    ["high", "high", "medium", 7 * .75 * 4 / 144],
    ["high", "high", "high", 7 * .75 / 144]
], [vsf.distribution, congestion.distribution, distance.distribution]), name="candidate")

# determine candidate nodes from information about transportation and distribution networks
