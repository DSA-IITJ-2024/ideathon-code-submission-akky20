[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/234bMY4A)

# Maximum Flow in a Metro System

This Python program implements algorithms to calculate the maximum flow in a metro system represented as a graph. It utilizes the Ford-Fulkerson algorithm with Dijkstra's algorithm for finding the shortest paths.

## Overview

The program consists of the following components:

1. `Edge` class: Represents an edge in the graph with attributes such as capacity, cost, and flow.
2. `Graph` class: Represents the metro system graph with methods to add edges and construct the adjacency list.
3. `dijkstra` function: Implements Dijkstra's algorithm to find the shortest paths from a source node.
4. `ford_fulkerson` function: Implements the Ford-Fulkerson algorithm to calculate the maximum flow in the graph.
5. `update_network` function: Updates the network with changes in edge capacities.
6. `reverse_update` function: Reverses the updates made to the network to restore the original state.
7. Main code: Defines the metro system graph, calculates the original maximum flow, and demonstrates the update process.

## Usage

To use the program:

1. Define the metro system graph by creating a `Graph` object and adding edges using the `add_edge` method.
2. Calculate the original maximum flow using the `ford_fulkerson` function.
3. Optionally, make changes to the network by updating edge capacities according to the required max flow or number of people.
4. Recalculate the maximum flow after updates using the `ford_fulkerson` function.
5. Print the results.

## Example

```python
# Define the metro system graph
n = 6  # Number of stations
graph = Graph(n)
# Add edges to the graph
# ...
# Calculate the original maximum flow
original_max_flow = ford_fulkerson(graph, source, sink)
print("Original Maximum Flow:", original_max_flow)
# Make changes to the network if needed
# ...
# Recalculate the maximum flow after updates
new_max_flow = 510
update_network(graph, reverse_update(graph, new_max_flow, original_edges))
# Print the results
print("New Maximum Flow:", new_max_flow)
