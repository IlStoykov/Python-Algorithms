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
from collections import deque
class Edges:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(" ")]
    graph.append(Edges(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edges in graph:
        if distance[edges.source] == float('inf'):
            continue
        new_distance = distance[edges.source] + edges.weight
        if new_distance < distance[edges.destination]:
            distance[edges.destination] = new_distance
            parent[edges.destination] = edges.source
            updated = True
    if not updated:
        break
for edges in graph:
    new_distance = distance[edges.source] + edges.weight
    if new_distance < distance[edges.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=" ")
    print(distance[target])
