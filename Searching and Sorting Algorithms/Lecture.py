"""binary search"""
# def binary_search(nums, target_num):
#     left_index = 0
#     right_index = len(nums) - 1
#
#     while True:
#         if target_num not in nums:
#             return -1
#         else:
#             target_index = nums.index(target_num)
#             midd_index = (left_index + right_index) // 2
#
#             if midd_index == target_index:
#                 return target_index
#
#             elif midd_index > target_index:
#                 right_index -= midd_index
#                 continue
#
#             elif midd_index < target_index:
#                 left_index += midd_index
#                 continue
#
#
# nums = [int(x) for x in input().split()]
# target_num = int(input())

# print(binary_search(nums, target_num))

# def binary_search(nums, target_num):
#     left_index = 0
#     right_index = len(nums) - 1
#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         mid_el = nums[mid_index]
#
#         if mid_el == target_num:
#             return mid_index
#
#         if target_num > mid_el:
#             left_index = mid_index + 1
#
#         else:
#             right_index = mid_index - 1
#     return -1
#
#
# nums = [int(x) for x in input().split()]
# target_num = int(input())
#
# print(binary_search(nums, target_num))