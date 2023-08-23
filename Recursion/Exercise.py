"""1.	Reverse Array"""
# def rev_array(arr):
#     if len(arr) == 1:
#         return arr
#     return rev_array(arr[1:]) + arr[0:1]
#
# arr = input().split()
# print(" ".join(rev_array(arr)))

"""2.	Nested Loops To Recursion"""
# def nested_loop(idx, vector, itr):
#     if idx >= len(vector):
#         print(*vector, sep=' ')
#         return
#     for i in range(1, itr + 1):
#         vector[idx] = i
#         nested_loop(idx + 1, vector, itr)
# itr = int(input())
# vector = [None] * itr
# nested_loop(0, vector, itr)

"""3.	Move Down / Right - count all possible paths"""
# def find_all_paths(row, col, rows, cols):
#     if row >= rows or col >= cols:
#         return 0
#     if row == rows - 1 and col == cols - 1:
#         return 1
#     result = 0
#     result += find_all_paths(row + 1, col, rows, cols)
#     result += find_all_paths(row, col + 1, rows, cols)
#
#     return result
#
# rows = int(input())
# cols = int(input())
#
# print(find_all_paths(0, 0, rows, cols))

"""4. Connected Areas in a Matrix - count all elements in 3D array"""

# class Area():
#     def __init__(self, c_row, c_col, c_size):
#         self.c_row = c_row
#         self.c_col = c_col
#         self.c_size = c_size
#
# def explore_matrix(row, col, matrix):
#     if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
#         return 0
#     if matrix[row][col] != "-":
#         return 0
#
#     matrix[row][col] = "v"
#
#     result = 1
#     result += explore_matrix(row - 1, col, matrix)
#     result += explore_matrix(row + 1, col, matrix)
#     result += explore_matrix(row, col - 1, matrix)
#     result += explore_matrix(row, col + 1, matrix)
#     return result
#
# rows = int(input())
# cols = int(input())
# matrix = []
# for _ in range(rows):
#     matrix.append(list(input()))
#
#
# arias = []
# for row in range(rows):
#     for col in range(cols):
#         size = explore_matrix(row, col, matrix)
#         if size == 0:
#             continue
#         else:
#             arias.append(Area(row, col, size))
#
# print(f"Total areas found: {len(arias)}")
# for idx, inventory in enumerate(sorted(arias, key = lambda x:x.c_size, reverse=True)):
#     print(f"Area #{idx + 1} at ({inventory.c_row}, {inventory.c_col}), size: {inventory.c_size}")




