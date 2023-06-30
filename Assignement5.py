Question 1
Convert 1D Array Into 2D Array
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []  

    result = []
    for i in range(m):
        row = original[i * n : (i + 1) * n]  
        result.append(row)

    return result


Question 2
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

def arrange_coins(n):
    k = 0  
    total = 0  
    while total + (k + 1) <= n:
        k += 1
        total += k

    return k

Question 3
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sorted_squares(nums):
    
    squared_nums = [num**2 for num in nums]
    sorted_nums = sorted(squared_nums)

    return sorted_nums


Question 4
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

def find_disjoint(nums1, nums2):
    set1 = set(nums1)  
    set2 = set(nums2)  

    diff1 = list(set1 - set2)  
    diff2 = list(set2 - set1)  

    return [diff1, diff2]

Question 5
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

def distance_value(arr1, arr2, d):
    distance = 0

    for num1 in arr1:
        has_close_element = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                has_close_element = True
                break

        if not has_close_element:
            distance += 1

    return distance

Question 6
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

def find_duplicates(nums):
    duplicates = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] *= -1

    return duplicates

Question 7
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

Question 8
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

import random

def find_original(changed):
    original = []
    count = {}
    
    for num in changed:
        if num % 2 == 1:
            return []
        original_num = num // 2
        original.append(original_num)
        count[original_num] = count.get(original_num, 0) + 1
    
    for num in original:
        if count.get(num, 0) != 2:
            return []
    
    random.shuffle(original)
    
    return original
