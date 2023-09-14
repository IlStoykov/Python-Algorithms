"""1.	Shortest Path in Unweighted Graph"""
# from collections import  deque
# nodes = int(input())
# edges = int(input())
#
# graph = []
# [graph.append([]) for _ in range(nodes + 1)]
#
# for _ in range(edges):
#     source, destination = [int(x) for x in input().split()]
#     graph[source].append(destination)
#
# start_node = int(input())
# destination_node = int(input())
#
# visited = [False] * (nodes + 1)
# parent = [None] * (nodes + 1)
#
# visited[start_node] = True
# queue = deque([start_node])
#
# while queue:
#     node = queue.popleft()
#     if node == destination_node:
#         break
#     for child in graph[node]:
#         if visited[child]:
#              continue
#         visited[child] = True
#         queue.append(child)
#         parent[child] = node
#
# result = deque()
# node = destination_node
# while node is not None:
#     result.appendleft(node)
#     node = parent[node]
# print(*result)

"""2.	Dijkstra's Algorithm"""
# Finding the shortest path between two nodes in an unweighted graph is done by applying simple BFS.
# from queue import PriorityQueue
# from collections import  deque
# class Edge:
#     def __init__(self, source, destination, weight):
#         self.source = source
#         self.destination = destination
#         self.weight = weight
#
#
# edges = int(input())
# graph = {}
# # reading and constructing graph with class for edges
# for _ in range(edges):
#     source, destination, weight = [int(x) for x in input().split(", ")]
#     if source not in graph:
#         graph[source] = []
#     if destination not in graph:
#         graph[destination] = []
#     graph[source].append(Edge(source, destination, weight))
#
# start = int(input())
# target = int(input())
# # find graph length and define graph distance [] and parent []
# max_node = max(graph.keys())
#
# distance = [float('inf')] * (max_node + 1)
# parent = [None] * (max_node + 1)
#
# distance[start] = 0
# # define priority queue and set start node there for bfs
# pq = PriorityQueue()
# pq.put((0, start))
#
# while not pq.empty():
#     min_distance, node = pq.get()
#     if node == target:
#         break
#     for edge in graph[node]:
#         # should check if new distance is smaller than exit and if it is change to new one
#         new_distance = min_distance + edge.weight
#         if new_distance < distance[edge.destination]:
#             # add the edge to pq with weight from prev nodes and it`s own weight
#             distance[edge.destination] = new_distance
#             parent[edge.destination] = node
#             pq.put((new_distance, edge.destination))
#
# if distance[target] == float ("inf"):
#     print('There is no such path. ')
# else:
#     print(distance[target])
#
#     path = deque()
#     node = target
#     while node is not None:
#         path.appendleft(node)
#         node = parent[node]
#     print(*path, end=" ")


"""3.	Bellman-Ford"""
# from collections import deque
# class Edges:
#     def __init__(self, source, destination, weight):
#         self.source = source
#         self.destination = destination
#         self.weight = weight
#
# nodes = int(input())
# edges = int(input())
#
# graph = []
#
# for _ in range(edges):
#     source, destination, weight = [int(x) for x in input().split(" ")]
#     graph.append(Edges(source, destination, weight))
#
# start = int(input())
# target = int(input())
#
# distance = [float('inf')] * (nodes + 1)
# distance[start] = 0
# parent = [None] * (nodes + 1)
#
# for _ in range(nodes - 1):
#     updated = False
#     for edges in graph:
#         if distance[edges.source] == float('inf'):
#             continue
#         new_distance = distance[edges.source] + edges.weight
#         if new_distance < distance[edges.destination]:
#             distance[edges.destination] = new_distance
#             parent[edges.destination] = edges.source
#             updated = True
#     if not updated:
#         break
# for edges in graph:
#     new_distance = distance[edges.source] + edges.weight
#     if new_distance < distance[edges.destination]:
#         print('Negative Cycle Detected')
#         break
# else:
#     path = deque()
#     node = target
#     while node is not None:
#         path.appendleft(node)
#         node = parent[node]
#     print(*path, sep=" ")
#     print(distance[target])

"""4.	Kruskal’s Algorithm"""
# class Edges:
#     def __init__(self, first, second, weight):
#         self.first = first
#         self.second = second
#         self.weight = weight
#
# def find_root(parent, node):
#     while node != parent[node]:
#         node = parent[node]
#     else:
#         return node
#
# graph = []
# edges = int(input())
#
# max_node = float("-inf")
# #define graph with classes and find max num for node
# for _ in range(edges):
#     first, second, weight = [int(x) for x in input().split(", ")]
#     graph.append(Edges(first, second, weight))
#     max_node = max(first, second, max_node)
#
# parent = [num for num in range(max_node + 1)]
# forest = []
#
# #work with sorted array
# for edge in sorted(graph, key=lambda x:x.weight):
#     # find root for first and second node
#     first_node_root = find_root(parent, edge.first)
#     second_node_root = find_root(parent, edge.second)
#     if first_node_root != second_node_root:
#         #merge first with the second node and become a part of the same tree
#         parent[first_node_root] = second_node_root
#         forest.append(edge)
# for edge in forest:
#     print(f"{edge.first} - {edge.second}")

"""5.	Prim's Algorithm"""
from queue import PriorityQueue
class Edges:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight
    #sorting edges by value
    def __gt__(self, other):
        return self.weight < other.weight
def prim(node, graph, forest, forrest_edges):
    #1. add the node to spann forest
    forest.add(node)
    #2. adding SORTED edges to priority queue
    pq = PriorityQueue()
    #3. put all edges in pq sorted ascending
    for edge in graph[node]:
        pq.put(edge)

    #4. getting all edges from the queue and check if one node in forest and other not
    while not pq.empty():
        #get the smallest el
        min_edge = pq.get()
        non_tree_node = -1
        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.second in forest and min_edge.second not in forest:
            non_tree_node = min_edge.first
        # if could not find a node out of the forest - continue
        if non_tree_node == -1:
            continue
        # else add non_tree_node to forest and all elements of non-tree_node add to pq and add forrest_edges to forrest_edges
        # because it is a part for min span tree
        forest.add(non_tree_node)
        forrest_edges.append(min_edge)
        for edge in graph[non_tree_node]:
            pq.put(edge)

graph = {}
edges = int(input())
for _ in range(edges):
    # forming graph with dictionary and adding all edges in keys of graph
    first, second, weight = [int(x) for x in input().split(", ")]
    if first not in graph:
        graph[first] = []
    elif second not in graph:
        graph[second] = []
    edge = Edges(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

""""collect all passed nodes"""
forest = set()
forrest_edges = []

# running Prim`s algorythm

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forrest_edges)
for edge in forrest_edges:
    print(f"{edge.first} - {edge.second}")
