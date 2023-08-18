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