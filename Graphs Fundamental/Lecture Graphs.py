"""Depth-First Search"""
# def dfs(node, graph, visited):
#     if node in visited:
#         return
#     visited.add(node)
#
#     for children in graph[node]:
#         dfs(children, graph, visited)
#     print(node, end=" ")
#
# graph = {
#     1:[19, 21, 14],
#     19:[7, 12, 31, 21],
#     7:[1],
#     12:[],
#     31:[21],
#     21:[14],
#     23:[21],
#     14:[6,23],
#     6:[]
# }
#
# visited = set()
# for node in graph:
#     dfs(node, graph, visited)

"""DFS for ordered node"""
# def dfs(node, graph, visited):
#
#     if node in visited:
#         return
#     visited.append(node)
#
#     for children in graph[node]:
#         dfs(children, graph, visited)
#     print(node, end=" ")
#
# graph = [
#     [6, 3],
#     [6, 3, 5, 2, 4],
#     [4, 1, 5],
#     [5, 1],
#     [6, 1, 2],
#     [1, 3, 2],
#     [0, 1, 4]
# ]
# visited = []
# for node in range(len(graph)):
#     dfs(node, graph, visited)

"""Breadth-First Search"""
# from collections import deque
#
# def bfs(node, graph, visited):
#     if node in visited:
#         return
#     queue = deque([node])
#     visited.append(node)
#
#     while queue:
#         current_node = queue.popleft()
#         print(current_node, end=" ")
#
#         for child in graph[current_node]:
#             if child not in visited:
#                 queue.append(child)
#                 visited.append(child)
# graph = {
#     7:[19, 21, 14],
#     19:[1, 12, 31, 21],
#     1:[7],
#     12:[],
#     31:[21],
#     21:[14],
#     14:[6, 23],
#     6:[],
#     23:[21]
# }
# visited = []
# for node in graph:
#     bfs(node, graph, visited)

"""Connected Components - DFS"""
# def dfs(node, visited, graph, component):
#     if node in visited:
#         return
#     visited.append(node)
#
#     for child in graph[node]:
#         dfs(child, visited, graph, component)
#
#     component.append(node)
#
# graph = []
# nodes = int(input())
# for node in range(nodes):
#     line = input()
#     child = [] if line == "" else [int(x) for x in line.split()]
#     graph.append(child)
#
# visited = []
#
# for node in range(nodes):
#     if node in visited:
#         continue
#     component = []
#     dfs(node, visited, graph, component)
#     print(f"Connected component: {' '.join([str(x) for x in component])}")
