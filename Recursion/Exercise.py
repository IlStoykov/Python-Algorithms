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
def find_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1
    result = 0
    result += find_all_paths(row + 1, col, rows, cols)
    result += find_all_paths(row, col + 1, rows, cols)

    return result

rows = int(input())
cols = int(input())

print(find_all_paths(0, 0, rows, cols))