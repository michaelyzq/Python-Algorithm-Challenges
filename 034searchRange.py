"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1]
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = list(reversed(nums))
        if target not in nums:
            return [-1,-1]
        return nums.index(target), len(nums2) -nums2.index(target)-1
        