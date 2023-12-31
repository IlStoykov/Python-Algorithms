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
#
# print(binary_search(nums, target_num))

"""Binary Search"""
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

"""Selection Sort"""
# def selct_sort(nums):
#     for idx in range(len(nums)):
#         first_number = nums[idx]
#         first_index = idx
#         for next_idx in range(idx + 1, len(nums)):
#             next_number = nums[next_idx]
#             if next_number < first_number:
#                 first_number = next_number
#                 first_index = next_idx
#                 nums[idx], nums[next_idx] = nums[next_idx], nums[idx]
#     return nums
#
# nums = [int(x) for x in input().split()]
# print(*selct_sort(nums), sep= " ")

"""Bubble Sort"""
# def bubble_sort(nums):
#     counter = 0
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for j in range(1, len(nums) - counter):
#             if nums[j] < nums[j - 1]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#                 is_sorted = False
#         counter += 1
#     return nums
# nums = [int(x) for x in input().split()]
# print(*bubble_sort(nums), sep=" ")

"""Insertion Sort"""
# def insert_sort(nums):
#     for i in range(len(nums)):
#         for j in range(i, 0, -1):
#             if nums[j] < nums[j -1]:
#                 nums[j], nums[j -1] = nums[j -1], nums[j]
#             else:
#                 break
#     return nums
# nums = [int(x) for x in input().split()]
# print(*insert_sort(nums), sep = " ")

"""Quicksort"""
"""selecting a pivot element and partitioning the array around the pivot, 
such that all elements less than the pivot are moved to its left and all elements greater than the pivot are moved to its right. 
Then, it recursively applies the same process to the left and right sub-arrays until the entire array is sorted."""
# def quicksort_funk(start, end, nums):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         if nums[left] > nums[pivot] > nums[right]:
#             nums[left], nums[right] = nums[right], nums[left]
#         if nums[left] <= nums[pivot]:
#             left += 1
#         if nums[right] >= nums[pivot]:
#             right -= 1
#
#     nums[right], nums[pivot] = nums[pivot], nums[right]
#     quicksort_funk(pivot, right - 1, nums)
#     quicksort_funk(left, end, nums)
#
# nums = [int(x) for x in input().split()]
# quicksort_funk(0, len(nums) -1, nums)
# print(*nums, sep = " ")

"""Merge Sort"""
# def merge_arrs(left_arr, right_arr):
#     result = [None] * (len(left_arr) + len(right_arr))
#     left_index = 0
#     right_index = 0
#     result_index = 0
#
#     while left_index < len(left_arr) and right_index < len(right_arr):
#         if left_arr[left_index] < right_arr[right_index]:
#             result[result_index] = left_arr[left_index]
#             left_index += 1
#         else:
#             result[result_index] = right_arr[right_index]
#             right_index += 1
#         result_index += 1
#
#     while left_index < len(left_arr):
#         result[result_index] = left_arr[left_index]
#         left_index += 1
#         result_index += 1
#
#     while right_index < len(right_arr):
#         result[result_index] = right_arr[right_index]
#         right_index += 1
#         result_index += 1
#
#     return  result
#
# def merge_sort(nums):
#     if len(nums) == 1:
#         return nums
#     mid_index = len(nums) // 2
#     left_arr = nums[:mid_index]
#     right_arr = nums[mid_index:]
#
#     return merge_arrs(merge_sort(left_arr),merge_sort(right_arr))
#
# nums = [int(x) for x in input().split()]
# result = merge_sort(nums)
# print(*result, sep=" ")

"""Merge Sort-Second"""
def merge_arr(left_arr, right_arr):
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1


    while left_index < len(left_arr):
        result.append(left_arr[left_index])
        left_index += 1

    while right_index < len(right_arr):
        result.append(right_arr[right_index])
        right_index += 1


    return result

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    midd_index = len(nums) // 2
    left_arr = nums[:midd_index]
    right_arr = nums[midd_index:]
    merge_arr(left_arr, right_arr)

nums = [int(x) for x in input().split()]
l_result = sorted(nums)
print(*l_result, sep=" ")