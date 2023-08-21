"""sum of list with nums with recursion"""
# def sum_array(nums, index):
#     if index == len(nums)-1:
#         return nums[index]
#     return nums[index] + sum_array(nums, index + 1)
#
# nums = [int(x) for x in input().split()]
# print(sum_array(nums, 0))

"""find factorials with recursion"""
# def calc_fact(n):
#     if n == 1:
#         return 1
#     return n * calc_fact(n-1)
# num = int(input())
# print (calc_fact(num))

"""drawing figure with recursion"""
# def draw_figure(n):
#     if n == 0:
#         return
#     print("*" * n)
#     draw_figure(n-1)
#     print("$" * n)
#
# n = int(input())
# draw_figure(n)

"""reverse a string with recursion"""
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))

"""counting and reverse counting with recursion"""
# def clac(n, start, result = 0):
#     if n == 0:
#         print (result)
#         return
#     start += 1
#     result += start
#     print (result)
#     clac(n - 1, start, result)
#     result -= start
#     print (result)
# n = int(input())
# clac(n, 0)

"""finding possible combinations with recursion"""
# def find_combinations(ind, vector):
#     if (ind >= len(vector)):
#         print(*vector, sep="")
#         return
#     for i in range(3):
#         vector[ind] = i
#         find_combinations(ind + 1, vector)
#
# n = int(input())
# vector = [None] * n
# find_combinations(0, vector)

""""finding the way out with backtracking"""
# def find_exit(row, col, lab, destination, path):
#     if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
#         return
#     if lab[row][col] == "*":
#         return
#     if lab[row][col] == "v":
#         return
#     path.append(destination)
#     if lab[row][col] == "e":
#         print("".join(path))
#
#     else:
#
#         lab[row][col] = "v"
#
#         find_exit(row - 1, col, lab, "U", path)
#         find_exit(row + 1, col, lab, "D", path)
#         find_exit(row, col - 1, lab, "L", path)
#         find_exit(row, col + 1, lab, "R", path)
#         lab[row][col] = "-"
#     path.pop()
#
# rows = int(input())
# cols = int(input())
# lab = []
# for _ in range(rows):
#     lab.append(list(input()))
#
# find_exit(0, 0, lab, "", [])

""" 8 Queens"""


def print_board(board):
    for row in board:
        print(" ".join(board))
    print()

def check_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonals:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def set_queen(row, col, rows, cols, left_diagonals, right_diagonals):
    pass


def put_queen(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if check_queen(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(row, col, rows, cols, left_diagonals, right_diagonals)
n = 8
board = []
[board.append("-" * 8) for _ in range(8)]
put_queen(row, board, set(), set(), set(), set())