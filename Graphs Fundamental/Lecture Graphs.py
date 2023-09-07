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

"""Source Removal Topological Sorting"""
# def find_dependencies(graph):
#     result = {}
#     for node, children in graph.items():
#         if node not in result:
#             result[node] = 0
#         for child in children:
#             if child not in result:
#                 result[child] = 1
#             else:
#                 result[child] += 1
#     return result
#
# """checking for 0 dendencies. if None cycle found"""
# def find_node_without_dependencies(dependencies_by_node):
#     for node, dependencies in dependencies_by_node.items():
#         if dependencies == 0:
#             return node
#     return None
#
# graph = {}
# nodes = int(input())
# for _ in range(nodes):
#     line = input().split("->")
#     node = line[0].strip()
#     children = line[1].strip().split(", ") if line[1] else []
#     graph[node] = children
#
# """finding each nods how much dependencies has"""
# dependencies_by_node = find_dependencies(graph)
# has_cycle = False
# result = []
#
# # finding node without dependencies
# while dependencies_by_node:
#     node_to_remove = find_node_without_dependencies(dependencies_by_node)
#     if node_to_remove is None:
#         has_cycle = True
#         break
#     dependencies_by_node.pop(node_to_remove)
#     result.append(node_to_remove)
#     for child in graph[node_to_remove]:
#         dependencies_by_node[child] -= 1
#
# if has_cycle:
#     print("Invalid topological sorting")
# else:
#     print(f"Topological sorting: {', '.join([str(x) for x in result])}")