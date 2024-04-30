import math

#Making the Graph
class Edge:
    def __init__(self, u, v, capacity, cost):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.cost = cost
        self.flow = 0

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.adj_list = [[] for _ in range(n)]
    
    def add_edge(self, u, v, capacity, cost):
        forward_edge = Edge(u, v, capacity, cost)
        backward_edge = Edge(v, u, 0, -cost)  
        self.edges.extend([forward_edge, backward_edge])
        self.adj_list[u].append(len(self.edges) - 2)  
        self.adj_list[v].append(len(self.edges) - 1)  



#Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = [math.inf] * graph.n
    predecessors = [-1] * graph.n
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        dist_u, u = queue.pop(0)
        if dist_u > distances[u]:
            continue
        for edge_index in graph.adj_list[u]:
            edge = graph.edges[edge_index]
            v = edge.v
            if edge.capacity - edge.flow > 0 and distances[u] + edge.cost < distances[v]:
                distances[v] = distances[u] + edge.cost
                predecessors[v] = edge_index
                queue.append((distances[v], v))
                queue.sort()
    return distances, predecessors


#Ford Fulkerson Algorithm for Max-Flow Concept
def ford_fulkerson(graph, start, destination):
    max_flow = 0
    while True:
        distances, predecessors = dijkstra(graph, start)
        if distances[destination] == math.inf:
            break
        path_flow = math.inf
        v = destination
        while v != start:
            edge_index = predecessors[v]
            edge = graph.edges[edge_index]
            path_flow = min(path_flow, edge.capacity - edge.flow)
            v = edge.u
        max_flow += path_flow
        v = destination
        while v != start:
            edge_index = predecessors[v]
            edge = graph.edges[edge_index]
            edge.flow += path_flow
            graph.edges[edge_index ^ 1].flow -= path_flow
            v = edge.u
    return max_flow

#Adjusting the Capacities of the Edges
def update_network(graph, changes):
    for change in changes:
        u, v, capacity_change = change
        for edge in graph.edges:
            if edge.u == u and edge.v == v:
                edge.capacity += capacity_change
                break
            
#Reversing the Update            
def reverse_update(graph, new_max_flow, original_edges):
    changes = []
    for edge in original_edges:
        u, v, capacity = edge
        for graph_edge in graph.edges:
            if graph_edge.u == u and graph_edge.v == v:
                adjusted_flow = graph_edge.flow * (new_max_flow / original_max_flow)
                capacity_change = new_max_flow - adjusted_flow
                changes.append((u, v, capacity_change))
    return changes

# Defining the metro system graph
n = 6  # Number of station
graph = Graph(n)
graph.add_edge(0, 1, 200, 5)   # Edge from station 0 to station 1, with capacity for 200 passengers and travel time of 5 minutes
graph.add_edge(0, 2, 150, 7)   # Edge from station 0 to station 2, with capacity for 150 passengers and travel time of 7 minutes
graph.add_edge(1, 2, 120, 3)   # Edge from station 1 to station 2, with capacity for 120 passengers and travel time of 3 minutes
graph.add_edge(1, 3, 180, 6)   # Edge from station 1 to station 3, with capacity for 180 passengers and travel time of 6 minutes
graph.add_edge(3, 2, 90, 4)    # Edge from station 3 to station 2, with capacity for 90 passengers and travel time of 4 minutes
graph.add_edge(2, 4, 160, 5)   # Edge from station 2 to station 4, with capacity for 160 passengers and travel time of 5 minutes
graph.add_edge(4, 3, 70, 3)    # Edge from station 4 to station 3, with capacity for 70 passengers and travel time of 3 minutes
graph.add_edge(3, 5, 220, 8)   # Edge from station 3 to station 5, with capacity for 220 passengers and travel time of 8 minutes
graph.add_edge(4, 5, 120, 4)   # Edge from station 4 to station 5, with capacity for 120 passengers and travel time of 4 minutes

# Defining the start and destination
start = 0
destination = 5

original_max_flow = ford_fulkerson(graph, start, destination)
print("People flow with Previous Edge Weight:", original_max_flow)

original_edges = [(0, 1, 200), (0, 2, 150), (1, 2, 120), (1, 3, 180),(3, 2, 90),(2, 4, 160),(4, 3, 70),(3, 5, 220),(4, 5, 120)]

# Enter the New FLow of People
new_max_flow = 510  



update_network(graph, reverse_update(graph, new_max_flow, original_edges))
altered_edges = reverse_update(graph, new_max_flow, original_edges)
altered_edges = [(t[0], t[1], round(t[2])) for t in altered_edges]

print(f"For People Flow of {new_max_flow}, required capacity:", altered_edges)

